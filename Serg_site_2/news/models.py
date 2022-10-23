from django.db import models

# Create your models here.

class News(models.Model):
    title=models.CharField(max_length=150)
    content=models.TextField(blank=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    photo=models.ImageField(upload_to='photos/%Y/%m/%d')
    is_published=models.BooleanField(default=True)

