from django.urls import path, include
from . import views


urlpatterns = [
    path('delivery/', views.DeliveryView.as_view()),
    path('delivery/<id>', views.DeliveryDetailView.as_view()),

    path('count/', views.CountView.as_view()),
]