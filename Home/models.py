from django.db import models

# Create your models here.
# 评论表
class ysof_comment(models.Model):
    content = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

