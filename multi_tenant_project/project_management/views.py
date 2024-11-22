from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import timedelta
from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer
from django.utils import timezone

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.filter(client=self.request.tenant)  # Filter by tenant

    @action(detail=True, methods=['get'])
    def analytics(self, request, pk=None):
        project = self.get_object()
        total_tasks = project.tasks.count()
        completed_tasks = project.tasks.filter(todo__completed=True).count()
        pending_tasks = total_tasks - completed_tasks
        overdue_tasks = project.tasks.filter(due_date__lt=timezone.now().date(), todo__completed=False).count()

        completed_tasks_with_time = project.tasks.filter(todo__completed=True, todo__completion_time__isnull=False)
        total_time = timedelta()
        if completed_tasks_with_time.exists():
            for task in completed_tasks_with_time:
                if task.todo.completion_time and task.todo.created_at:
                    time_diff = task.todo.completion_time - task.todo.created_at
                    total_time += time_diff
            average_completion_time = total_time / completed_tasks_with_time.count()
        else:
            average_completion_time = None

        analytics = {
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "pending_tasks": pending_tasks,
            "overdue_tasks": overdue_tasks,
            "average_completion_time": average_completion_time,
        }
        return Response(analytics)

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(client=self.request.tenant)  # Filter by tenant

    