from django.urls import path, include
from . import views


urlpatterns = [
    path('task-item/', views.TaskItemView.as_view()),
    path('task-item/<id>', views.TaskItemDetailView.as_view()),    

    path('count/', views.CountView.as_view()),
    path('annotate/', views.AnnotateView.as_view()),
]
