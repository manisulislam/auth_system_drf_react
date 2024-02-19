from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import UserRegisterSerializer, LogInSerializer
from rest_framework.response import Response
from rest_framework import status
from .utils import send_code_to_user
from .models import OneTimePassword
# Create your views here.


class UserRegisterView(GenericAPIView):
    serializers_class=UserRegisterSerializer

    def post(self, request):
        user_data=request.data
        serializer=UserRegisterSerializer(data=user_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user=serializer.data
            #send to email for user['email']
            send_code_to_user(user['email'])

            return Response({
                'data':user,
                'message':f"hi, Thank you for sign up, a passcode has to be sent"
            },status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class VerifyUserEmail(GenericAPIView):
    def post(self, request):
        optCode=request.data.get("otp")
        try:
            user_code_object=OneTimePassword.objects.get(code=optCode)
            user=user_code_object.user
            if not user.is_verified:
                user.is_verified=True
                user.save()
                return Response({
                    "message":"account verified successful"
                },status=status.HTTP_200_OK)
            return Response({
                "message":"code is invalid. user already verified"
            }, status=status.HTTP_204_NO_CONTENT)
        except OneTimePassword.DoesNotExist:
            return Response({
                "message":"passcode is not provided"
            }, status=status.HTTP_404_NOT_FOUND)


class LogInUserView(GenericAPIView):
    serializers_class=LogInSerializer
    def post(self, request):
        serializer=self.serializers_class(data=request.data, context={"request":request})
        serializer.is_valid(raise_exception=True)
        # serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
