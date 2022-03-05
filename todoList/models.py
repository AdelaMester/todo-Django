from django.db import models

# Create your models here.
class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    hash_password = models.CharField(max_length=200)

class Tasks(models.Model):
    task_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)
    completed = models.CharField(max_length=10)