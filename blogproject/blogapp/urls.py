from django.urls import path
from .views import LoginList

urlpatterns = [
    path('login/create/', LoginList.as_view(), name='login_create'),
    # Add more patterns as needed
]
