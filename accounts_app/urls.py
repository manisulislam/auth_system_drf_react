from django.urls import path
from .views import UserRegisterView,VerifyUserEmail, LogInUserView,PasswordResetRequestView,PasswordResetConfirm,SetNewPassword,LogoutUserView,TestAuthenticationView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns=[
    path('register/',UserRegisterView.as_view(),name='register'),
    path('verify-email/', VerifyUserEmail.as_view(), name='verify-email' ),
    path('login/',LogInUserView.as_view(), name='login'),
    path('password-reset/', PasswordResetRequestView.as_view(), name='password-reset'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('password-reset-confirm/<uidb64>/<token>/',PasswordResetConfirm.as_view(), name='password-reset-confirm'),
    path('set-new-password/', SetNewPassword.as_view(), name='set-new-password'),
    path('logout/',LogoutUserView.as_view(), name='logout'),
    path('test-auth/', TestAuthenticationView.as_view(), name='test-auth'),
]
