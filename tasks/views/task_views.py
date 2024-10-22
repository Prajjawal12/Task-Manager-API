from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from tasks.models.task import Task
from tasks.serializers.task_serializer import TaskSerializer
from tasks.serializers.task_serializer import AssignTaskSerializer
from tasks.models.user import User

class CreateTaskView(APIView):
    """
    API view to create a new task.

    This view handles POST requests to create a new task.
    It expects a JSON body with task details.

    Methods:
        post(request):
            Creates a new task with the provided details.
    """
    def post(self, request):
        """
        Creates a new task based on the provided request data.

        Parameters:
            request: The request object containing the HTTP request data.

        Returns:
            Response: A Response object containing the serialized task data
                      if the creation is successful, or an error message if
                      validation fails.
        """
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the task instance
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AssignTaskView(APIView):
    """
    API view to assign users to a specific task.

    This view handles POST requests to assign specified users to the given task.
    It expects a JSON body with 'user_ids' and 'task_id'.

    Methods:
        post(request):
            Assigns specified users to the specified task.
    """
    def post(self, request):
        """
        Assigns users to the specified task based on the provided user IDs and task ID.

        Parameters:
            request: The request object containing the HTTP request data.

        Returns:
            Response: A Response object containing a success message if users are
                      assigned successfully, or an error message if the task or
                      users are not found or if validation fails.
        """
        serializer = AssignTaskSerializer(data=request.data)
        if serializer.is_valid():
            user_ids = serializer.validated_data['user_ids']
            task_id = serializer.validated_data['task_id']  # Use task_id for fetching the task

            # Fetch users and validate
            users = User.objects.filter(id__in=user_ids)
            if not users.exists():
                return Response({"error": "No valid users found"}, status=status.HTTP_404_NOT_FOUND)

            # Fetch the task and validate
            try:
                task = Task.objects.get(id=task_id)
            except Task.DoesNotExist:
                return Response({"error": "The task does not exist."}, status=status.HTTP_404_NOT_FOUND)

            # Assign users to the task
            task.assigned_users.set(users, clear=True)  # Clear previous assignments to avoid duplicates
            task.save()

            return Response({
                "message": "Users assigned to the task successfully"
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
