from rest_framework import serializers
from tasks.models.task import Task
from tasks.models.user import User
from tasks.serializers.user_serializer import UserSerializer

class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for representing tasks, including the users assigned to each task.

    This serializer handles the validation and serialization of Task model instances,
    converting them to and from JSON format. It includes all fields necessary to represent
    a task except for the assigned_users field during task creation.

    Attributes:
        Meta:
            Contains the configuration for the serializer, including the
            model it is based on and the fields to be serialized.
    """

    class Meta:
        model = Task  # The model that this serializer is associated with
        fields = ['id', 'name', 'description', 'created_at', 'updated_at', 'status', 'task_type']  # Fields to be serialized


class AssignTaskSerializer(serializers.Serializer):
    """
    Serializer for assigning users to a single task.

    This serializer validates the input data for assigning users to a task,
    ensuring that the user IDs and task ID provided exist in the database.

    Fields:
        - user_ids: List of user IDs to assign to a task.
        - task_id: ID of the task to which users will be assigned.
    """
    user_ids = serializers.ListField(
        child=serializers.IntegerField(),
        allow_empty=False,
        help_text="List of user IDs to assign"
    )
    task_id = serializers.IntegerField(
        help_text="ID of the task to assign users to"
    )

    def validate_user_ids(self, value):
        """
        Custom validation for user_ids.

        Ensures that all provided user IDs exist in the database. If any
        user ID does not exist, a ValidationError is raised.

        Parameters:
            value: List of user IDs to validate.

        Returns:
            value: The validated list of user IDs.

        Raises:
            serializers.ValidationError: If one or more user IDs do not exist.
        """
        if not User.objects.filter(id__in=value).exists():
            raise serializers.ValidationError("One or more users do not exist.")
        return value

    def validate_task_id(self, value):
        """
        Custom validation for task_id.

        Ensures that the provided task ID exists in the database. If the
        task ID does not exist, a ValidationError is raised.

        Parameters:
            value: The task ID to validate.

        Returns:
            value: The validated task ID.

        Raises:
            serializers.ValidationError: If the task ID does not exist.
        """
        if not Task.objects.filter(id=value).exists():
            raise serializers.ValidationError("The task does not exist.")
        return value
