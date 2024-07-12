from django.contrib import admin
from .models import User, Community, Camera, User_Community, Camera_Community

# Register your models here.


admin.site.register(Community)
admin.site.register(Camera)
admin.site.register(User_Community)
admin.site.register(Camera_Community)