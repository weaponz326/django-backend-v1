from django.urls import path, include
from . import views


urlpatterns = [
    path('task-group/', views.TaskGroupView.as_view()),
    path('task-group/<id>', views.TaskGroupDetailView.as_view()),
    path('all-task-item/', views.AllTaskItemView.as_view()),
    path('task-item/', views.TaskItemView.as_view()),
    path('task-item/<id>', views.TaskItemDetailView.as_view()),

    path('count/', views.CountView.as_view()),
    path('annotate/', views.AnnotateView.as_view()),
]
