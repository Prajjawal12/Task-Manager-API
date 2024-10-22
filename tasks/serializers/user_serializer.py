from rest_framework import serializers
from tasks.models.user import User

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.

    This serializer handles the validation and serialization of User
    model instances, converting them to and from JSON format.

    Attributes:
        Meta:
            Contains the configuration for the serializer, including the
            model it is based on and the fields to be serialized.
    """

    class Meta:
        model = User  # The model that this serializer is associated with
        fields = ['id', 'name', 'email', 'mobile', 'created_at']  # Fields to be serialized
