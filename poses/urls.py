from django.urls import path
from .views import (
     PosRegisterView, PosRegisterDetailView, PosRegisterListView
)
urlpatterns = [
    #Parents
    # path('parents/', ParentListView.as_view(), name='Parents'),
    # path('parents/<int:pk>/', ParentDetailView.as_view(),name='Parent_detail'),

    #posRegister
    # path('Parents/<int:Parent_id>/poses/',  PosRegisterListView.as_view(),name='poses'),
    # path('Parents/<int:Parent>/poses/<int:pk>/',  PosRegisterDetailView.as_view(),name='poses-detail'),
    path('api/poses/pos-register/',  PosRegisterView.as_view(),name='pos-register'),
    path('api/poses/pos-list/',  PosRegisterListView.as_view(),name='pos-list'),
    path('api/poses/<int:pk>/',  PosRegisterDetailView.as_view(),name='poses-detail'),
]