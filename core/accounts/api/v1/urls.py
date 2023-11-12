from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)



app_name = "accounts-api-v1"





urlpatterns = [
    # registration
    path('registration/', views.RegistrationApiView.as_view(), name='registration'),
    # token
    path('token/login/', views.CustomobtainAuthToken.as_view(), name='token-login'),
    path('token/logout/', views.CustomDiscardAuthToken.as_view(), name='token-logout'),
    # jwt
    path('jwt/create/', views.CustomTokenObtainPairView.as_view(), name='jtw-create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jtw-refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='token-verify'),
    # change password
    path('change-password/', views.ChangePasswordApiView.as_view(), name='change-password'),
    # profile
    path('profile/', views.ProfileApiView.as_view(), name='profile'), 
    # email
    path('verfication-email', views.VerficationEmailApiView.as_view(), name='verfication-email'),
    path('activation/confirm/<str:token>',views.ActivationApiView.as_view(), name='activation' ),
    path('activation/resend/', views.ActivationResendApiView.as_view(), name='activation-resend' ),   
]