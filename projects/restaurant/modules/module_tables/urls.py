from django.urls import path, include
from . import views


urlpatterns = [
    path('table/', views.TableView.as_view()),
    path('table/<id>', views.TableDetailView.as_view()),

    path('count/', views.CountView.as_view()),
]