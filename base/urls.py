from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, UpdateTask, DeleteTask, CustomLoginView, CustomRegisterView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('register/', CustomRegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('task-detail/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>', UpdateTask.as_view(), name='task-update'),
    path('task-delete/<int:pk>', DeleteTask.as_view(), name='task-delete'),

    
]
