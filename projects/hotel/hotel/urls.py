"""hotel URL Configuration

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

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('accounts.urls')),
    path('module-admin/', include('modules.module_admin.urls')),
    path('module-portal/', include('modules.module_portal.urls')),
    path('module-settings/', include('modules.module_settings.urls')),
    # path('module-bills/', include('modules.module_bills.urls')),
    # path('module-staff/', include('modules.module_staff.urls')),
    # path('module-guests/', include('modules.module_guests.urls')),
    # path('module-roster/', include('modules.module_roster.urls')),
    # path('module-payments/', include('modules.module_payments.urls')),
    # path('module-services/', include('modules.module_services.urls')),
    # path('module-checkin/', include('modules.module_checkin.urls')),
    # path('module-bookings/', include('modules.module_bookings.urls')),
    # path('module-rooms/', include('modules.module_rooms.urls')),
    # path('module-assets/', include('modules.module_assets.urls')),
    # path('module-housekeeping/', include('modules.module_housekeeping.urls')),
]
