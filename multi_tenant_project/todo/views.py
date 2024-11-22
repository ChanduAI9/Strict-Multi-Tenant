from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer,UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    

    def get_queryset(self):
        return Todo.objects.filter(client=self.request.tenant)
    
    #current tenant
    # def perform_create(self,)



class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)