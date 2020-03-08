from django.shortcuts import render
from rest_framework import generics, permissions, views, response, status
from django.contrib.auth import get_user_model
from user.models import AuthToken
from user.serializer import UserLoginSerializer
import uuid

User = get_user_model()

class UserLogin(generics.GenericAPIView):
    """
    Use this end-point to authenticate a user and generate an auth token.

    **Url**
        ``/users/login/``

    **Permissions**
        - Any is allowed.

    **Post**
        - Validate via Serializer
        - Generate Auth Token

    **Finalize Response**
        - From database get or create an auth token.
        - Set authorization into cookie with finalize_response.
    """
    serializer_class = UserLoginSerializer
    permission_classes = (
        permissions.AllowAny,
    )

    def post(self, request):
        """
        If serializer is valid.
            - call action.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.get(username=serializer.validated_data.get('username'))
            token_obj, boolean = AuthToken.objects.get_or_create(user=user)
            print (boolean, "NEWUSERRRRRRRRR")
            if boolean:
                token_obj.token = str(uuid.uuid4())
                token_obj.save()
            return response.Response(
                data=token_obj.token,
                status=status.HTTP_200_OK,)
        return response.Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)
