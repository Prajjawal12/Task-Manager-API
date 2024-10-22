from django.urls import path
from tasks.views.task_views import CreateTaskView, AssignTaskView
from tasks.views.create_user_view import CreateUserView
from tasks.views.user_views import GetTasksForUserView, GetUsersForTaskView

urlpatterns = [
    path('api/tasks/', CreateTaskView.as_view(), name='create_task'),
    path('api/tasks/assign/', AssignTaskView.as_view(), name='assign-tasks'),
     path('api/users/<int:user_id>/tasks/', GetTasksForUserView.as_view(), name='get-tasks-for-user'),
      path('api/tasks/<int:task_id>/users/', GetUsersForTaskView.as_view(), name='get-users-for-task'),
    path('api/users/',CreateUserView.as_view(),name='create_user')

]
