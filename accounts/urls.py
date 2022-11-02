from django.urls import path
from .views import AccountLoginView, AccountLogoutView, account_view

app_name = 'accounts'

urlpatterns = [
    path('login/', AccountLoginView.as_view(), name='login'),
    path('logout/', AccountLogoutView.as_view(), name='logout'),
    path('profile/', account_view, name='profile'),
]
