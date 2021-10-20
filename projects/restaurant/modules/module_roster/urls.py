from django.urls import path, include
from . import views


urlpatterns = [
    path('roster/', views.RosterView.as_view()),
    path('roster/<id>', views.RosterDetailView.as_view()),
    path('shift/', views.ShiftView.as_view()),
    path('shift/<id>', views.ShiftDetailView.as_view()),
    path('batch/', views.BatchView.as_view()),
    path('batch/<id>', views.BatchDetailView.as_view()),
    path('refresh-personnel/', views.RefreshPersonnelView.as_view()),
    path('personnel/', views.StaffPersonnelView.as_view()),
    path('personnel/<id>', views.StaffPersonnelDetailView.as_view()),
    path('refresh-sheet/', views.RefreshSheetView.as_view()),
    path('roster-day/', views.RosterDayView.as_view()),
    path('roster-sheet/', views.RosterSheetView.as_view()),

    path('count/', views.CountView.as_view()),
]
