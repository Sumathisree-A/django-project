from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from .tasks import send_welcome_email

@api_view(['POST'])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        send_welcome_email.delay(user.username, user.email)
        return Response({'message': 'User registered and email sent!'}, status=201)
    return Response(serializer.errors, status=400)
