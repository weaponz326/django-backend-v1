"""association URL Configuration

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
    # path('module-members/', include('modules.module_members.urls')),
    # path('module-committees/', include('modules.module_committees.urls')),
    # path('module-dues/', include('modules.module_dues.urls')),
    # path('module-executives/', include('modules.module_executives.urls')),
    # path('module-action-plan/', include('modules.module_action_plan.urls')),
    # path('module-budget/', include('modules.module_budget.urls')),
    # path('module-attendance/', include('modules.module_attendance.urls')),
    # path('module-meetings/', include('modules.module_meetings.urls')),
    # path('module-groups/', include('modules.module_groups.urls')),
    # path('module-year/', include('modules.module_year.urls')),
]
