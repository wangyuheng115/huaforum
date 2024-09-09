from django.shortcuts import render
from . models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from . serializer import *
from django.contrib.auth import authenticate, login,get_user_model
from django.contrib.auth.hashers import check_password
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from uuid import uuid4
from django.core.files.storage import default_storage


# Create your views here.
User = get_user_model()
class UserView(APIView):
    serializer_class = ReactSerializer

    def get(self, request):
        details = [
            {
                "userid": detail.userid,
                "username": detail.username,
                "usernicname": detail.usernicname,
            }
            for detail in ysof_users.objects.all()
        ]
        return Response(details)

    def post(self, request):
        print("This is post")
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

class LoginView(APIView):
    serializer_class = ReactSerializer

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        User = get_user_model()
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({"message": "User does not exist"}, status=400)
        #user = User.objects.get(username=username)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            #login(request, user)
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            print(token)
            return Response({"token": token})
        else:
            return Response({"message": "Invalid credentials"}, status=400)
    
class UserInfoView(APIView):
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        # 在这里处理需要身份验证的视图逻辑
        user_data = {
            "usernicname": user.usernicname,
            "useravatar": user.useravatar.url if user.useravatar else None,
            "usernote": user.usernote if user.usernote else None,
            "userbirthday": user.userbirthday if user.userbirthday else None,
            "usersex": user.usersex,
            "userwx": user.userwx if user.userwx else None,
            "userqq": user.userqq if user.userqq else None,
            "usernumber": user.usernumber if user.usernumber else None,
        }
        return Response(user_data)

class UserAvatarView(APIView):
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        print(request.FILES.get('avatar'))
        if request.method == 'POST' and request.FILES.get('avatar'):
            avatar_file = request.FILES['avatar']

            # 生成用户专属头像名以防重名
            file_name = f"{request.user.userid}_{uuid4().hex}_{avatar_file.name}"
            # 保存文件到服务器
            user = request.user  # 假设已经通过身份验证获取了用户对象

            # 获取旧头像路径
            old_avatar = user.useravatar.name

            # 保存新头像
            user.useravatar.save(file_name, avatar_file, save=True)

            # 删除旧头像文件
            if old_avatar:  # 确保用户有旧头
                default_storage.delete(old_avatar)

            # 返回成功响应
            return Response({'avatarUrl': user.useravatar.url})

        return Response({'error': '只接受 POST 请求且必须包含 avatar 字段'}, status=400)

class SaveProfileView(APIView):
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def put(self, request):
        user = request.user
        serializer = ProfileSerializer(user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)