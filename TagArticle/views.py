from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ysof_tagarticle

# Create your views here.
class SearchTagView(APIView):
    def get(self, request, *args, **kwargs):

        # 获取查询参数
        query = request.query_params.get('tagName', '')

        if query:
            # 使用icontains进行模糊查询，查找tadescri中包含查询内容的记录
            results = ysof_tagarticle.objects.filter(tadescri__icontains=query)

            # 将查询结果转换为字典列表
            data = [{"taid": result.taid, "tadescri": result.tadescri, "created_at": result.created_at} for result in
                    results]

            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Query parameter 'tagName' is required."}, status=status.HTTP_400_BAD_REQUEST)

class SearchSingleTagView(APIView):
    def get(self, request, *args, **kwargs):

        # 获取查询参数
        query = request.query_params.get('tagName', '')

        if query:
            # 使用icontains进行模糊查询，查找tadescri中包含查询内容的记录
            results = ysof_tagarticle.objects.filter(tadescri__exact=query)

            # 将查询结果转换为字典列表
            data = [{"taid": result.taid, "tadescri": result.tadescri, "created_at": result.created_at} for result in
                    results]

            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Query parameter 'tagName' is required."}, status=status.HTTP_400_BAD_REQUEST)

class CreateTagView(APIView):
    def post(self, request, *args, **kwargs):
        # 获取请求体中的标签内容
        tadescri = request.data.get('tagName', '')

        if not tadescri:
            return Response({"message": "Tag content 'tagName' is required."}, status=status.HTTP_400_BAD_REQUEST)

        # 创建新标签
        new_tag = ysof_tagarticle.objects.create(tadescri=tadescri)

        # 将创建的标签信息返回给用户
        data = {
            "taid": new_tag.taid,
            "tadescri": new_tag.tadescri,
            "created_at": new_tag.created_at,
        }

        return Response(data, status=status.HTTP_201_CREATED)