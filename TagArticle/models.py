from django.db import models

# Create your models here.
#文章标签表
class ysof_tagarticle(models.Model):
    taid = models.BigAutoField(primary_key=True) #标签id
    tadescri = models.TextField() #标签内容
    created_at = models.DateTimeField(auto_now_add=True, null=True) #创建时间
