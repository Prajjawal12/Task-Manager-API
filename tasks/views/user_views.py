from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from tasks.models.user import User
from tasks.models.task import Task
from tasks.serializers.task_serializer import TaskSerializer
from tasks.serializers.user_serializer import UserSerializer

class GetTasksForUserView(APIView):
    """
    API view to retrieve tasks assigned to a specific user.

    This view handles GET requests to retrieve all tasks associated
    with a user identified by their user ID.

    Methods:
        get(request, user_id):
            Retrieves tasks for the specified user.
    """
    def get(self, request, user_id):
        """
        Retrieves tasks for the specified user.

        Parameters:
            request: The request object containing the HTTP request data.
            user_id: The ID of the user for whom to retrieve tasks.

        Returns:
            Response: A Response object containing the serialized task data
                      or an error message if the user is not found.
        """
        try:
            user = User.objects.get(id=user_id)
            tasks = user.tasks.all()  # Fetch all tasks associated with the user
            serializer = TaskSerializer(tasks, many=True)  # Serialize the task data
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({
                "error": "User not found"
            }, status=status.HTTP_404_NOT_FOUND)

class GetUsersForTaskView(APIView):
    """
    API view to retrieve users assigned to a specific task.

    This view handles GET requests to retrieve all users who are
    assigned to a task identified by its task ID.

    Methods:
        get(request, task_id):
            Retrieves users assigned to the specified task.
    """
    def get(self, request, task_id):
        """
        Retrieves users assigned to the specified task.

        Parameters:
            request: The request object containing the HTTP request data.
            task_id: The ID of the task for which to retrieve assigned users.

        Returns:
            Response: A Response object containing the serialized user data
                      or an error message if the task is not found.
        """
        try:
            task = Task.objects.get(id=task_id)  # Fetch the task by ID
            users = task.assigned_users.all()  # Get users assigned to this task
            serializer = UserSerializer(users, many=True)  # Serialize the user data
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response({
                "error": "Task not found"
            }, status=status.HTTP_404_NOT_FOUND)
