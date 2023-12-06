from django.urls import path
from .views import LoginCreate##,LoginListView, LoginDetailView, LoginUpdateView

urlpatterns = [
    path('create',LoginCreate.as_view(),name='login'),
    # path('login/list/', LoginListView.as_view(), name='login_list'),
    # path('login/detail/<int:pk>/', LoginDetailView.as_view(), name='login_detail'),
    # path('login/update/<int:pk>/', LoginUpdateView.as_view(), name='login_update'),
    # # # Add other URL patterns if needed
]