"""
URL configuration for project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# this will import the built-in login view
from django.contrib.auth import views as auth_views
from django.urls import path, include
# done to avoid confusion as views is common
from users import views as user_views
# these are for displaying images
from django.conf import settings
from django.conf.urls.static import static

# good practice to sort them alphabetically 
urlpatterns = [
    # this is saying go to blog -> urls.py
    # if we keep the '' empty it will show blogs home as a front page no need for the user to type
    # or go to blog/
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),
    path('register/', user_views.register, name='register'),
]

# TO DISPLAY IMAGES
# if we are in debug mode, meaning development mode as when in production it is off
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #this means, bring stuff from MEDIA_ROOT and give us their urls MEDIA_URL
