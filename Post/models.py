from django.db import models
from django.contrib.auth.models import User
# from django.convert import NoneType
# Create your models here.
from django.db.models.deletion import get_candidate_relations_to_delete
import datetime
from django.utils import timezone
# datetime.datetime.now()
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=50)
    content = models.TextField(default='')
    img = models.ImageField(upload_to='post_img/', default='post_img/default.png')
    created = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.title