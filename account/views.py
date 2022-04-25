from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from .models import UserProfile
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages


def index(request):
    return render(request, "property/index.html")


def signupform(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("index")
    else:
        return render(request, "account/signupform.html")


def signupsubmit(request):
    if request.POST.get("password") != request.POST.get("password2"):
        messages.error(request, "Passwords Don't Match. Try Again!")
        return render(request, "account/signupform.html")
    try:
        UserProfile.objects.get(username=request.POST.get("username"))
        messages.error(
            request, "Username Already Exists, Please Select A Unique Username!"
        )
        return render(request, "account/signupform.html")
    except Exception:
        first_name = request.POST["fname"]
        last_name = request.POST["lname"]
        username = request.POST["username"]
        # TODO validate email
        email = request.POST["email"]
        phone = request.POST["phone"]
        password = request.POST["password"]
        # uid = request.user.id # TODO: doesnt work since user is anonymous first and request has no ID (since not logged in)

        # TODO BUG UNIQUE constraint failed: UserProfile.username

        user = UserProfile.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            phone=phone,
            password=password,
            email=email,
        )
        user.save()
        subject = "Welcome to House ME!"
        message = "Congratulations! Your email ID has been authenticated. You can now go back to the login page."
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False,
        )
        return render(request, "account/loginform.html")


def loginform(request):
    return render(request, "account/loginform.html")


def loginsubmit(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        print("sucess")
        return HttpResponseRedirect(reverse("property:browselistings"))
    else:
        print("wrong password")
        messages.error(request, "Wrong password or username, please check")
        return render(request, "account/loginform.html")


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data["email"]
            associated_users = UserProfile.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "account/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        # TODO Change the domain address
                        "domain": "houseme-app.herokuapp.com",
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


# def profile(request, slug=None):
#     account = None
#     if slug:
#         account = UserProfile.objects.get(username=slug)

#     return render(request, "account/profile.html", {"account": account})


def profile(request, username):
    account = UserProfile.objects.get(username=username)
    return render(request, "account/profile.html", {"account": account})


@login_required(login_url="/account/loginform")
def edit(request):
    account = UserProfile.objects.get(username=request.user.username)
    return render(request, "account/edit.html", {"account": account})
