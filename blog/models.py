import uuid
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    content = models.TextField()
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title
