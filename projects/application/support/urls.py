from django.urls import path, include
from . import views


urlpatterns = [
    path('support-contact/', views.SupportContactView.as_view()),
    path('support-contact/<id>', views.SupportContactDetailView.as_view()),
]