from django.db import models
from Article.models import ysof_articles

# Create your models here.
class ysof_images(models.Model):
    imid = models.BigAutoField(primary_key=True)
    impath = models.ImageField(upload_to='articles/', null=True, blank=True)
    imarticleid = models.ForeignKey(ysof_articles, on_delete=models.CASCADE)
