from django.urls import path
from .views import UserRegisterView,VerifyUserEmail, LogInUserView,PasswordResetRequestView,PasswordResetConfirm,SetNewPassword,LogoutUserView

urlpatterns=[
    path('register/',UserRegisterView.as_view(),name='register'),
    path('verify-email/', VerifyUserEmail.as_view(), name='verify-email' ),
    path('login/',LogInUserView.as_view(), name='login'),
    path('password-reset/', PasswordResetRequestView.as_view(), name='password-reset'),
    path('password-reset-confirm/<uidb64>/<token>/',PasswordResetConfirm.as_view(), name='password-reset-confirm'),
    path('set-new-password/', SetNewPassword.as_view(), name='set-new-password'),
    path('logout/',LogoutUserView.as_view(), name='logout')
]
