#import the necessary modules
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("", views.index, name="index"),
    path("hello", views.HelloView.as_view(), name="hello_view" ),
    path ("token_auth_generate", obtain_auth_token, name="token_generation"),       #Getting token for already created users.
    path("signup", views.Signup, name="signup"),
]