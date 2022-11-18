from django.urls import path
from .views import (
    UserListView, UserDetailView, PosRegisterListView, PosRegisterDetailView
)
urlpatterns = [
    #users
    path('users/', UserListView.as_view(), name='users'),
    path('users/<int:pk>/', UserDetailView.as_view(),name='user_detail'),

    #posRegister
    path('users/<int:user>/poses/',  PosRegisterListView.as_view(),name='poses'),
    path('users/<int:user>/poses/<int:pk>/',  PosRegisterDetailView.as_view(),name="poses-detail"),
]