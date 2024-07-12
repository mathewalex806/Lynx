from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='app1_user_set',  # Add related_name to avoid conflicts
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='app1_user_set',  # Add related_name to avoid conflicts
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    def __str__(self):
        return self.username


#Adding Community table

class Community (models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=50,blank=False, null=False)
    locality = models.CharField(max_length=50)
    country = models.CharField(max_length=70, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


