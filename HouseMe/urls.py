"""HouseMe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from typing import List

from account import views as account_view
from account.models import User


class UsersListView(LoginRequiredMixin, ListView):
    http_method_names = [
        "get",
    ]

    def get_queryset(self):
        return User.objects.all().exclude(id=self.request.user.id)

    def render_to_response(self, context, **response_kwargs):
        users: List[AbstractBaseUser] = context["object_list"]

        data = [{"username": user.get_username(), "pk": str(user.pk)} for user in users]
        return JsonResponse(data, safe=False, **response_kwargs)


urlpatterns = [
    path("property/", include("Property.urls")),
    path("admin/", admin.site.urls),
    path("register/", account_view.register, name="register"),
    path("profile/", account_view.profile, name="profile"),
    path("", include("Property.urls")),
    path("account/", include("account.urls", namespace="account")),
    path("users/", UsersListView.as_view(), name="users_list"),
    re_path(
        r"", include("django_private_chat2.urls", namespace="django_private_chat2")
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
