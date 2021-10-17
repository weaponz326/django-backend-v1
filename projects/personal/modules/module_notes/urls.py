from django.urls import path, include
from . import views


urlpatterns = [
    path('note/', views.NoteView.as_view()),
    path('note/<id>', views.NoteDetailView.as_view()),
    path('file/', views.NoteFileView.as_view()),
    path('file/<id>', views.NoteFileDetailView.as_view()),

    path('count/', views.CountView.as_view()),
    path('date-annotate/', views.DateAnnotateView.as_view()),

]
