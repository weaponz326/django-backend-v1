"""shop URL Configuration

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
    # path('module-receivables/', include('modules.module_receivables.urls')),
    # path('module-products/', include('modules.module_products.urls')),
    # path('module-invoice/', include('modules.module_invoice.urls')),
    # path('module-marketting/', include('modules.module_marketting.urls')),
    # path('module-payables/', include('modules.module_payables.urls')),
    # path('module-sales/', include('modules.module_sales.urls')),
    # path('module-customers/', include('modules.module_customers.urls')),
    # path('module-payments/', include('modules.module_payments.urls')),
    # path('module-orders/', include('modules.module_orders.urls')),
    # path('module-inventory/', include('modules.module_inventory.urls')),
    # path('module-suppliers/', include('modules.module_suppliers.urls')),
    # path('module-purchasing/', include('modules.module_purchasing.urls')),
    # path('module-cashflow/', include('modules.module_cashflow.urls')),
    # path('module-staff/', include('modules.module_staff.urls')),
]
