from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class ysof_users(AbstractUser):
    userid = models.BigAutoField(primary_key=True)
    usernicname = models.CharField(max_length=32)
    userbirthday = models.DateField(null=True)
    usernote = models.TextField(default="请输入你的简介~")
    userdevice = models.CharField(max_length=10, null=True)
    userip = models.CharField(max_length=24, null=True)
    userqq = models.CharField(max_length=18, null=True, unique=True)
    userwx = models.CharField(max_length=32, null=True, unique=True)
    usernumber = models.CharField(max_length=18, null=True, unique=True)
    usersex = models.IntegerField(null=True,default=0)
    useravatar = models.ImageField(upload_to='useravatars/', null=True, blank=True)
    userlevel = models.IntegerField(null=True)
    modified_at = models.DateTimeField(auto_now=True)

    # Add related_name to avoid clashes with the built-in User model
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='ysof_users_groups',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='ysof_users_permissions',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )