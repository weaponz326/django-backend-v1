"""personal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('rest-auth/', include('rest_framework.urls')),
    path('accounts/', include('allauth.urls')),

    path('users/', include('users.urls')),
    path('module-calendar/', include('modules.module_calendar.urls')),
    path('module-notes/', include('modules.module_notes.urls')),
    path('module-accounts/', include('modules.module_accounts.urls')),
    path('module-budget/', include('modules.module_budget.urls')),
    path('module-tasks/', include('modules.module_tasks.urls')),
    path('module-portal/', include('modules.module_portal.urls')),
    path('module-settings/', include('modules.module_settings.urls')),
]
