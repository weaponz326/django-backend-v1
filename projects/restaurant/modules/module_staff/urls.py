from django.urls import path, include
from . import views


urlpatterns = [
    path('staff/', views.StaffView.as_view()),
    path('staff/<id>', views.StaffDetailView.as_view()),
]