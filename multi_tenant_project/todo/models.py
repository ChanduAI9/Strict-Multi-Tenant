from django.db import models
from tenants.models import Client
from django.utils import timezone

class Todo(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)  # Link to tenant schema
    title = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    recurrence_interval = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completion_time = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.completed and not self.completion_time:
            self.completion_time = timezone.now()
        elif not self.completed:
            self.completion_time = None
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title
