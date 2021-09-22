"""school URL Configuration

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
    # path('module-parents/', include('modules.module_parents.urls')),
    # path('module-assessment/', include('modules.module_assessment.urls')),
    # path('module-attendance/', include('modules.module_attendance.urls')),
    # path('module-students/', include('modules.module_students.urls')),
    # path('module-reports/', include('modules.module_reports.urls')),
    # path('module-teachers/', include('modules.module_teachers.urls')),
    # path('module-staff/', include('modules.module_staff.urls')),
    # path('module-payments/', include('modules.module_payments.urls')),
    # path('module-classes/', include('modules.module_classes.urls')),
    # path('module-timetable/', include('modules.module_timetable.urls')),
    # path('module-fees/', include('modules.module_fees.urls')),
    # path('module-sections/', include('modules.module_sections.urls')),
]
