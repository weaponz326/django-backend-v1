from django.urls import path, include
from . import views


urlpatterns = [
    path('task/', views.TaskView.as_view()),
    path('task/<id>', views.TaskDetailView.as_view()),
]
