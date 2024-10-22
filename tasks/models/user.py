from django.db import models

class User(models.Model):
    """
    User model to represent a user in the system.

    This model contains all necessary fields for user information,
    including name, email, mobile number, and creation timestamp.

    Attributes:
        id (AutoField): Unique identifier for each user.
        name (CharField): The name of the user, with a maximum length of 100 characters.
        email (EmailField): The email address of the user, must be unique.
        mobile (CharField): The mobile number of the user, must be unique and have a maximum length of 10 characters.
        created_at (DateTimeField): Timestamp indicating when the user was created, automatically set on creation.
    """

    id = models.AutoField(primary_key=True)  # Unique identifier for each user
    name = models.CharField(max_length=100)  # User's name
    email = models.EmailField(unique=True)  # User's email address (must be unique)
    mobile = models.CharField(max_length=10, unique=True)  # User's mobile number (must be unique)

    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the user was created

    def __str__(self):
        """
        String representation of the User model.

        Returns:
            str: The name of the user, used when the object is printed.
        """
        return self.name
