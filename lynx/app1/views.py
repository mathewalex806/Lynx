from django.shortcuts import render
from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserSerializer
from .models import *
from django.contrib.auth.models import User
# Create your views here.


#Function based view 
def index(request):
    return HttpResponse("Request recieved in the app.")

#class based view
class HelloView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content, status=status.HTTP_200_OK)

## SIGN UP method    
@api_view(["POST","GET"])
@permission_classes([AllowAny])
def Signup(request):
    if request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()                                                   ##Calls the create user method in the serializer
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    return HttpResponse("Get url for signup")