from django.urls import path
from .views import PosRegisterListView , UserView

urlpatterns = [
    path('poses/',  PosRegisterListView.as_view()),
    path('users/', UserView.as_view()),
]