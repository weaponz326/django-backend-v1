from django.urls import path, include
from . import views


urlpatterns = [
    path('account/', views.AccountView.as_view()),
    path('account/<id>', views.AccountDetailView.as_view()),

    path('search/', views.SearchListView.as_view()),
    path('search/<id>', views.SearchDetailView.as_view()),

    path('has-account/', views.HasAccountView.as_view()),
    path('active-account/', views.ActiveAccountView.as_view()),
    path('user-accounts/', views.UserAccountsView.as_view()),
]
