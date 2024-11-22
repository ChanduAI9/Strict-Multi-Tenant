from django.db import models
from django.contrib.auth.models import User
from tenants.models import Client
from todo.models import Todo

class Project(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)  # tenant schema
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Task(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)  # tenant schema
    project = models.ForeignKey(Project, related_name="tasks", on_delete=models.CASCADE)
    todo = models.ForeignKey(Todo, related_name="tasks", on_delete=models.CASCADE)
    assigned_user = models.ForeignKey(User, related_name="assigned_tasks", on_delete=models.SET_NULL, null=True, blank=True)
    due_date = models.DateField()

    def __str__(self):
        return f"Task for projects:{self.project.name}"
