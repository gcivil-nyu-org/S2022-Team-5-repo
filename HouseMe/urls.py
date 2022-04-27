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
from django.urls import path, include
from account import views as account_view
from django.conf.urls.static import static
from django.conf import settings
from chat import views as chat_view

urlpatterns = [
    path("property/", include("Property.urls")),
    path("admin/", admin.site.urls),
    path("register/", account_view.register, name="register"),
    path("profile/", account_view.profile, name="profile"),
    path("", include("Property.urls")),
    path("account/", include("account.urls", namespace="account")),
    path("chat/", chat_view.chatPage, name="chat"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
