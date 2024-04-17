from django.urls import path
from .views import *
from .views import RegisterView,LoginView,UserListView

urlpatterns = [

    path('user/register/', RegisterView.as_view(), name='register'),
    path('user/login/', LoginView.as_view(), name='login'),
    path('users/', UserListView.as_view(), name='user-list'),

    path('rides/', RideListView.as_view(), name='ride-list'),
    path('rides/create/', RideCreateView.as_view(), name='ride-create'),
    path('rides/<int:pk>/', RideDetailView.as_view(), name='ride-detail'),
    path('rides/status/update/<int:pk>/', RideStatusUpdateView.as_view(), name='ride-update-status'),

    path('test/', TestCreateView.as_view(), name='test'),
]
