from django.urls import path
from .views import (
    TaskListCreateAPIView,
    TaskDetailAPIView,
    TaskStatusUpdateAPIView
)


urlpatterns = [
    path("tasks/", TaskListCreateAPIView.as_view()),
    path("tasks/<int:pk>/", TaskDetailAPIView.as_view()),
    path("tasks/<int:pk>/status/", TaskStatusUpdateAPIView.as_view()),

]
