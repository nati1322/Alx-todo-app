from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    def mark_as_complete(self, request, pk=None):
        try:
            todo = self.get_object()
            todo.completed = True
            todo.save()
            serializer = self.get_serializer(todo)
            return Response(serializer.data)
        except Todo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def mark_as_incomplete(self, request, pk=None):
        try:
            todo = self.get_object()
            todo.completed = False
            todo.save()
            serializer = self.get_serializer(todo)
            return Response(serializer.data)
        except Todo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)