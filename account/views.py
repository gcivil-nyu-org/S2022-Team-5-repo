from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes


from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import User


def loginform(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            print("sucess")
            return HttpResponseRedirect(reverse("property:index"))
        else:
            print("wrong password")
            messages.error(request, "Wrong password or username, please check")
            return render(request, "account/loginform.html")
    return render(request, "account/loginform.html")


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data["email"]
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "account/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        # TODO Change the domain address
                        "domain": "housieme.herokuapp.com",
                        "site_name": "Website",
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        "token": default_token_generator.make_token(user),
                        "protocol": "http",
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        # send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
                        send_mail(
                            subject=subject,
                            message=email,
                            from_email=settings.EMAIL_HOST_USER,
                            recipient_list=[user.email],
                            fail_silently=False,
                        )
                    except BadHeaderError:
                        return HttpResponse("Invalid header found.")
                    return redirect("password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(
        request=request,
        template_name="account/password_reset.html",
        context={"password_reset_form": password_reset_form},
    )


def sign_out(request):
    """
    Basic view for user sign out
    """
    logout(request)
    return redirect(reverse("account:loginform"))


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.phone = form.cleaned_data.get("phone_number")
            user.save()
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            messages.success(request, f"Account created for {username}!")
            subject = "Welcome to House ME!"
            message = "Congratulations! Your email ID has been authenticated. You can now go back to the login page."
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False,
            )
            return redirect("account:loginform")
    else:
        form = UserRegisterForm()
    return render(request, "account/register.html", {"form": form})


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES or None, instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your account has been updated!")
            return redirect("profile")

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {"u_form": u_form, "p_form": p_form}

    return render(request, "account/profile.html", context)
