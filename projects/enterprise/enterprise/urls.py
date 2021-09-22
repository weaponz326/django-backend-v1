"""enterprise URL Configuration

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
    # path('module-accounts/', include('modules.module_accounts.urls')),
    # path('module-payroll/', include('modules.module_payroll.urls')),
    # path('module-attendance/', include('modules.module_attendance.urls')),
    # path('module-assets/', include('modules.module_assets.urls')),
    # path('module-leave/', include('modules.module_leave.urls')),
    # path('module-budget/', include('modules.module_budget.urls')),
    # path('module-procurement/', include('modules.module_procurement.urls')),
    # path('module-letters/', include('modules.module_letters.urls')),
    # path('module-appraisal/', include('modules.module_appraisal.urls')),
    # path('module-files/', include('modules.module_files.urls')),
    # path('module-employees/', include('modules.module_employees.urls')),
    # path('module-ledger/', include('modules.module_ledger.urls')),
    # path('module-reception/', include('modules.module_reception.urls')),
]
