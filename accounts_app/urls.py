from django.urls import path
from .views import UserRegisterView,VerifyUserEmail, LogInUserView

urlpatterns=[
    path('register/',UserRegisterView.as_view(),name='register'),
    path('verify_email/', VerifyUserEmail.as_view(), name='verify_email' ),
    path('login/',LogInUserView.as_view(), name='login')
]
