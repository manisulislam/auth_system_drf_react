from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import UserRegisterSerializer
from rest_framework.response import Response
from rest_framework import status
from .utils import send_code_to_user
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

