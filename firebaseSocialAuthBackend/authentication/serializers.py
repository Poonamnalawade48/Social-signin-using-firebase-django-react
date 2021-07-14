from rest_framework import serializers

from authentication.models import CustomUser


class SocialUserSerializer(serializers.ModelSerializer):
    """
    class to serialize the user details login through social media
    """

    class Meta:
        model = CustomUser
        fields = ["id", "email", "name", "image"]

    def create(self, validated_data):
        """
        Function for creating and returning the created instance
         based on the validated data of the user.
        """

        user = CustomUser.objects.create_user(
            name=validated_data.pop('name'),
            email=validated_data.pop('email'),

        )
        return user


class AddSocialUidSerializer(serializers.ModelSerializer):
    """
    serializer to add/update uid to user model
    """

    class Meta:
        model = CustomUser
        fields = ['id', 'uid']
