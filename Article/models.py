from django.db import models
from User.models import ysof_users

# Create your models here.
class ysof_articles(models.Model):
    arid = models.BigAutoField(primary_key=True) #文章ID
    artitle = models.CharField(max_length=51)   #文章标题
    arcover = models.ImageField(upload_to='articlescover/', null=True, blank=True)  #文章封面
    arcontent = models.TextField()  #文章内容
    arprivate = models.IntegerField(null=True,default=0) #文章访问权限
    archeck = models.IntegerField(null=True, default=0) #文章审核状态
    arview = models.IntegerField(null=True, default=0)  #文章观看数
    arlike = models.IntegerField(null=True, default=0)  #文章点赞数
    arsave = models.IntegerField(null=True, default=0)  #文章收藏数
    arshare = models.IntegerField(null=True, default=0) #文章分享数
    arcomment = models.IntegerField(null=True, default=1)   #文章评论权限
    artags = models.TextField(default='') #文章标签
    modified_at = models.DateTimeField(auto_now=True)   #文章最后修改时间
    uploaded_at = models.DateTimeField(auto_now=True)   #文章创建时间
    aruserid = models.ForeignKey(ysof_users, on_delete=models.CASCADE)  #文章用户归属