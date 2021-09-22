"""production URL Configuration

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
    # path('module-stock/', include('modules.module_stock.urls')),
    # path('module-equipment/', include('modules.module_equipment.urls')),
    # path('module-purchasing/', include('modules.module_purchasing.urls')),
    # path('module-orders/', include('modules.module_orders.urls')),
    # path('module-manufacturing/', include('modules.module_manufacturing.urls')),
    # path('module-contractors/', include('modules.module_contractors.urls')),
    # path('module-projects/', include('modules.module_projects.urls')),
    # path('module-workers/', include('modules.module_workers.urls')),
    # path('module-tasks/', include('modules.module_tasks.urls')),
    # path('module-roster/', include('modules.module_roster.urls')),
    # path('module-materials/', include('modules.module_materials.urls')),
]
