from django.urls import path
from .views import ProfileView, UserRegistrationView, user_registration_view_done
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
path('profile/<str:user_name>', ProfileView.as_view(), name='profile'),
path('login/', LoginView.as_view(), name='login'),
path('logout/', LogoutView.as_view(), name='logout'),
path('password_change/', PasswordChangeView.as_view(), name='password_change'),
path('password_change_done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
path('password_reset_done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
path('password_reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
path('password_reset_complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
path('user_registration/', UserRegistrationView.as_view(), name='user_registration'),
path('user_registration_done/', user_registration_view_done, name='user_registration_done'),
]