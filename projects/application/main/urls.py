from django.urls import path, include
from . import views


urlpatterns = [
    path('user-source/', views.UserSourceView.as_view()),
]
