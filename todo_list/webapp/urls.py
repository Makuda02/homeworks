from django.urls import path
from .views import IndexView, TaskView, TaskCreateView, TaskDeleteView, TaskUpdateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('task/add/', TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/', TaskView.as_view(), name='task-detail'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update_view'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete_view'),
]
