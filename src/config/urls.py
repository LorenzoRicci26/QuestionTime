"""
URL configuration for questiontime project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import include, path
from core.views import IndexTemplateView
from users.forms import CustomUserRegistrationForm
from django_registration.backends.one_step.views import RegistrationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')), # Django's built-in auth URLs
    path('auth/', include('djoser.urls')),  # Djoser URLs for user management
    path('auth/', include('djoser.urls.authtoken')),  # Djos

    path(
        'accounts/register/', 
        RegistrationView.as_view(form_class=CustomUserRegistrationForm, success_url = "/"), 
        name='django_registration_register'),

    path('accounts/', include('django.contrib.auth.urls')), # Django's built-in auth URLs for login/logout
    path('', IndexTemplateView.as_view(), name='entrypoint'),  # Home page
]
