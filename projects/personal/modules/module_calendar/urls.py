from django.urls import path, include
from . import views

urlpatterns = [
    path('appointment/', views.AppointmentView.as_view()),
    path('appointment/<id>', views.AppointmentDetailView.as_view()),
]
