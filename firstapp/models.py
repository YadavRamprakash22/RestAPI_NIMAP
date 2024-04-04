from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    client_name=models.CharField(max_length=300)
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.client_name


class Project(models.Model):
    project_name=models.CharField(max_length=100)
    client=models.ForeignKey(Client, on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='assigned_users')
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User, on_delete=models.CASCADE)