from django.shortcuts import render
from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.permissions import IsAuthenticated
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