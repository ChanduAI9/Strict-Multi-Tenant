from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'register': reverse('register', request=request, format=format),
        'todos': reverse('todo-list', request=request, format=format),
        'projects': reverse('project-list', request=request, format=format),
        'tasks': reverse('task-list', request=request, format=format),
    })
