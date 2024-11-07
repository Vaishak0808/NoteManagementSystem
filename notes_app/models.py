from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length=255,blank = True,null = True)
    body = models.TextField(blank = True,null = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes',blank = True,null = True)
    created_at = models.DateTimeField(auto_now_add=True,blank = True,null = True)
    updated_at = models.DateTimeField(auto_now=True,blank = True,null = True)

    def __str__(self):
        return self.title
