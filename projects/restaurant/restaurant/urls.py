"""restaurant URL Configuration

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
    path('module-menu/', include('modules.module_menu.urls')),
    path('module-staff/', include('modules.module_staff.urls')),
    path('module-tables/', include('modules.module_tables.urls')),
    path('module-customers/', include('modules.module_customers.urls')),
    path('module-deliveries/', include('modules.module_deliveries.urls')),
    path('module-payments/', include('modules.module_payments.urls')),
    path('module-roster/', include('modules.module_roster.urls')),
    path('module-reservations/', include('modules.module_reservations.urls')),
    path('module-orders/', include('modules.module_orders.urls')),
    path('module-kitchen-stock/', include('modules.module_kitchen_stock.urls')),
    path('module-sittings/', include('modules.module_sittings.urls')),
]
