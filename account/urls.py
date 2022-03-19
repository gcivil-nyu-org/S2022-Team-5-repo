from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path("loginform", views.loginform, name="loginform"),
    path("loginsubmit", views.loginsubmit, name="loginsubmit"),
    path("signupform", views.signupform, name="signupform"),
    path("signupsubmit", views.signupsubmit, name="signupsubmit"),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="account/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="account/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="account/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]
