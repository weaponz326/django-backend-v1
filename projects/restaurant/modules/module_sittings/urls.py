from django.urls import path, include
from . import views


urlpatterns = [
    path('sitting/', views.SittingView.as_view()),
    path('sitting/<id>', views.SittingDetailView.as_view()),
]
