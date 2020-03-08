
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserLoginSerializer(serializers.Serializer):
    """
    Serializer User login

    **Validate**
        - validate user exists with given username
        - Use UserService to verify credentials.

    **Create**
        - None
    """

    username = serializers.CharField()

    password = serializers.CharField(
        style={'input_type': 'password'})

    def validate(self, data):
        username = data.get('username').lower()
        password = data.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            raise serializers.ValidationError(
                "Validation Error User doesn't exist")
        if not user.check_password(password):
            raise serializers.ValidationError(
                "Validation Error User doesn't exist")
        # print (data, "SERIALZER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return data

    class Meta:
        fields = ('username', 'password')
