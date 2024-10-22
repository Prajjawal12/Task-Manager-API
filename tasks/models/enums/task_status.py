# Choices for task status in the application.
# This enumeration defines the different states a task can be in.

TASK_STATUS_CHOICES = [
    ('pending', 'Pending'),        # Task is yet to be started
    ('in_progress', 'In Progress'),  # Task is currently being worked on
    ('completed', 'Completed'),      # Task has been finished
    ('archived', 'Archived')         # Task is archived and no longer active
]
