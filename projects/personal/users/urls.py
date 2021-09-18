from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

    path('search/', views.SearchListView.as_view()),
    path('search/<id>', views.SearchDetailView.as_view()),
]
