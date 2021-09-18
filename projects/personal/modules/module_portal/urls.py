from django.urls import path, include
from . import views


urlpatterns = [
    path('rink/', views.RinkView.as_view()),
    path('rink/<id>', views.RinkDetailView.as_view()),
    path('rink-list/', views.RinkListView.as_view()),
    path('count-rink-date/', views.CountRinkDateListView.as_view()),
]
