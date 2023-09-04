"""
URL configuration for percy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from videos_account.views import (
    videos,
    staff_dashboard,
    upload_content,
    manage_content,
)
    
from user_account.views import(
    login_view,
    signup_view,
    logout_view,
    #custom_password_reset,
    #reset_password,
)

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('videos/', videos, name='videos'),
    
    path('', login_view, name='login-User'),
    path('register/',signup_view, name="register"),
    path('logout/', logout_view, name="logout"),

    # Password reset URLs
    #path('reset_password/', reset_password, name='reset_password'),
    #path('password_reset_user/', custom_password_reset, name='password_reset_user'),

    #staffs urls only
    path('dashboard/', staff_dashboard, name='dashboard'),
    path('upload_content/', upload_content, name='upload_content'),
    path('manage_content/', manage_content, name='manage_content'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)