from rest_framework import serializers
from . models import *
from datetime import datetime
from django.contrib.auth.hashers import make_password

class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ysof_users
        fields = [
            'userid',
            'username',
            'usernicname',
            'password'
        ]

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = ysof_users(**validated_data)
        user.set_password(password)
        user.save()
        return user

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ysof_users
        fields = [
            'usernicname',
            'usernote',
            'userbirthday',
            'usersex',
            'userwx',
            'userqq',
            'usernumber',
            'modified_at',
        ]

    def update(self, instance, validated_data):
        instance.modified_at = datetime.now()
        return super().update(instance, validated_data)