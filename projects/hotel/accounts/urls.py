from django.urls import path, include
from . import views


urlpatterns = [
    path('profile/', views.ProfileView.as_view()),
    path('profile/<int:pk>', views.ProfileDetailView.as_view()),
]