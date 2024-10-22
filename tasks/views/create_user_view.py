from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from tasks.models.user import User
from tasks.serializers.user_serializer import UserSerializer

class CreateUserView(APIView):
    """
    API view to create a new user.

    This view handles POST requests to create a new user.
    It expects a JSON body with user details such as username, email, etc.

    Methods:
        post(request):
            Creates a new user with the provided details.
    """

    def post(self, request):
        """
        Creates a new user based on the provided request data.

        Parameters:
            request (Request): The request object containing the HTTP request data.

        Returns:
            Response: A Response object containing a success message and the
                      serialized user data if the creation is successful,
                      or an error message if validation fails.
        """
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()  # Save the new user instance
            return Response({
                "message": "User created successfully",
                "user": UserSerializer(user).data  # Return serialized user data
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return validation errors
