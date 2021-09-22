"""hospital URL Configuration

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
    path('modules-admin/', include('modules.module_admin.urls')),
    path('modules-portal/', include('modules.module_portal.urls')),
    path('modules-settings/', include('modules.module_settings.urls')),
    # path('modules-patients/', include('modules.module_patients.urls')),
    # path('modules-appointments/', include('modules.module_appointments.urls')),
    # path('modules-staff/', include('modules.module_staff.urls')),
    # path('modules-bills/', include('modules.module_bills.urls')),
    # path('modules-doctors/', include('modules.module_doctors.urls')),
    # path('modules-laboratory/', include('modules.module_laboratory.urls')),
    # path('modules-payments/', include('modules.module_payments.urls')),
    # path('modules-nurses/', include('modules.module_nurses.urls')),
    # path('modules-prescriptions/', include('modules.module_prescriptions.urls')),
    # path('modules-diagnosis/', include('modules.module_diagnosis.urls')),
    # path('modules-drugs/', include('modules.module_drugs.urls')),
    # path('modules-wards/', include('modules.module_wards.urls')),
    # path('modules-admissions/', include('modules.module_admissions.urls')),
    # path('modules-dispensary/', include('modules.module_dispensary.urls')),
    # path('modules-roster/', include('modules.module_roster.urls')),
]
