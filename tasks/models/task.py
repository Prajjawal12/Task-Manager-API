from django.utils import timezone
from django.db import models
from .enums.task_status import TASK_STATUS_CHOICES
from .user import User

class Task(models.Model):
    """
    Task model to represent a task in the system.

    This model includes all necessary fields to describe a task,
    including its name, description, creation and update timestamps,
    type, status, and users assigned to it.

    Attributes:
        id (AutoField): Unique identifier for each task.
        name (CharField): The name of the task, must be unique, with a maximum length of 255 characters.
        description (TextField): Detailed description of the task.
        created_at (DateTimeField): Timestamp indicating when the task was created, automatically set on creation.
        updated_at (DateTimeField): Timestamp indicating when the task was last updated, automatically set on each update.
        task_type (CharField): Type of the task, with a default value of "work".
        status (CharField): Current status of the task, with predefined choices from TASK_STATUS_CHOICES and a default of 'pending'.
        assigned_users (ManyToManyField): Users assigned to the task, related to the User model, can be blank.
    """

    id = models.AutoField(primary_key=True)  # Unique identifier for each task
    name = models.CharField(max_length=255, unique=True)  # Task name (must be unique)
    description = models.TextField()  # Detailed description of the task
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the task was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for when the task was last updated
    task_type = models.CharField(max_length=100, default="work")  # Type of the task (default is 'work')
    status = models.CharField(max_length=20, choices=TASK_STATUS_CHOICES, default='pending')  # Current task status
    assigned_users = models.ManyToManyField(User, related_name='tasks', blank=True)  # Users assigned to the task

    def __str__(self):
        """
        String representation of the Task model.

        Returns:
            str: The name of the task, used when the object is printed.
        """
        return self.name
