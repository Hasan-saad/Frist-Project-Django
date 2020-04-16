from django.db import models
from django.contrib.auth.models import User
class post(models.Model):
    # user = models.ForeignKey(User,on_delete=None) 
    phone = models.IntegerField(default=' ')
    content = models.TextField(default=' ')
    

