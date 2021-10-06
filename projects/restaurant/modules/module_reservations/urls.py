from django.urls import path, include
from . import views


urlpatterns = [
    path('reservation/', views.ReservationView.as_view()),
    path('reservation/<id>', views.ReservationDetailView.as_view()),
]
