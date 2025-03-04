from django.urls import path
from .views import register_view, login_view, logout_view, email_confirm

urlpatterns = [
    path('register/', register_view, name = 'register'),
    path('login/', login_view, name = 'login'),
    path('logout/', logout_view, name = 'logout'),
    path('confirm-email/<uidb64>/<token>/', email_confirm, name='confirm_email'),
]