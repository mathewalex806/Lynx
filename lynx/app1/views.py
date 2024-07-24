from django.shortcuts import render
from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserSerializer, CameraSerializer
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
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


##LOGIN method
@api_view(["POST","GET"])
@permission_classes([AllowAny])
def Login(request):
    if request.method == "POST":
        username = request.data["username"]
        password = request.data["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, "message":"Login successfull"}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
    return HttpResponse("GET url for login page")

##Add Camera fuction

@api_view(["GET","POST"])
@permission_classes([IsAuthenticated])
def addCamera(request):
    if request.method == "POST":
        camera_ser = CameraSerializer(data=request.data)
        if camera_ser.is_valid():
            camera_ser.save()
            return Response({'Successfully created':camera_ser.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error':camera_ser.error_messages}, status=status.HTTP_400_BAD_REQUEST)
    return Response({'Get method': 'Add_camera url'}, status=status.HTTP_200_OK)