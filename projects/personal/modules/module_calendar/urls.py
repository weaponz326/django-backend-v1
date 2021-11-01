from django.urls import path, include
from . import views

urlpatterns = [
    path('calendar/', views.CalendarView.as_view()),
    path('calendar/<id>', views.CalendarDetailView.as_view()),
    path('schedule/', views.ScheduleView.as_view()),
    path('schedule/<id>', views.ScheduleDetailView.as_view()),

    path('count/', views.CountView.as_view()),
    path('annotate/', views.AnnotateView.as_view()),
]
