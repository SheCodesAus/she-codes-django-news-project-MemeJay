from django.urls import path
from .views import CreateAccountView, ProfileView, get_current_user

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('user-profile/<int:pk>', ProfileView.as_view(), name='userProfile'),
    path('user-profile/', get_current_user, name='currentUser'),
]