from django.urls import path, include
from . import views


urlpatterns = [
    path('stock-item/', views.StockItemView.as_view()),
    path('stock-item/<id>', views.StockItemDetailView.as_view()),
]