from django.urls import path, include
from . import views

urlpatterns = [
    path('user/', views.UserView.as_view()),
    path('user/<id>', views.UserDetailView.as_view()),
    path('user-access/', views.AccessView.as_view()),
    path('user-access/<id>', views.AccessDetailView.as_view()),
    path('invitation/', views.InvitationView.as_view()),
    path('invitation/<id>', views.InvitationDetailView.as_view()),
]
