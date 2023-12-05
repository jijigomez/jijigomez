from django.urls import path
from .views import LoginCreateView

urlpatterns = [
    path('login/create/', LoginCreateView.as_view(), name='login_create'),
    # Add more patterns as needed
]
