from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Task
from .serializers import TaskSerializer


class TaskListCreateAPIView(APIView):

    def get(self, request):
     status_param = request.query_params.get("status")

     qs = Task.objects.all()

     if status_param:
         qs = qs.filter(status=status_param)

     qs = qs.order_by("-created_at")

     serializer = TaskSerializer(qs, many=True)
     return Response(serializer.data)


    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        task = serializer.save()
        return Response(
            TaskSerializer(task).data,
            status=status.HTTP_201_CREATED
        )


class TaskDetailAPIView(APIView):

    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def delete(self, request, pk):
     if not Task.objects.filter(id=pk).exists():
        return Response(
            {"detail": "Task not found"},
            status=status.HTTP_404_NOT_FOUND
        )

     Task.objects.filter(id=pk).delete()
     return Response(status=status.HTTP_204_NO_CONTENT)

