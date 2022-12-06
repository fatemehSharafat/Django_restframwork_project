from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


from .views import LoginView, GetTokenView

urlpatterns = [
    path('api/login/', LoginView.as_view(), name='login'),
    path('get-token/', GetTokenView.as_view(), name='register'),

    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]