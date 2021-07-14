from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView

from .models import CustomUser
from .serializers import SocialUserSerializer
from .utils import firebase_validation, ResponseInfo


class SocialSignupAPIView(GenericAPIView):
    """
    api for creating user from social logins
    """

    authentication_classes = ()
    permission_classes = ()
    serializer_class = SocialUserSerializer

    def __init__(self, **kwargs):
        """
         Constructor function for formatting the web response to return.
        """
        self.response_format = ResponseInfo().response
        super(SocialSignupAPIView, self).__init__(**kwargs)

    def post(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION')

        if auth_header:
            id_token = auth_header.split(" ").pop()

            validate = firebase_validation(id_token)

            if validate:
                user = CustomUser.objects.filter(uid=validate["uid"]).first()

                if user:
                    data = {
                        "id": user.id,
                        "email": user.email,
                        "name": user.name,
                        "image": user.image,
                        "type": "existing_user",
                        "provider": validate['provider']
                    }

                    self.response_format["data"] = data
                    self.response_format["status_code"] = status.HTTP_201_CREATED
                    self.response_format["error"] = None
                    self.response_format["message"] = "User already exist"
                else:
                    user = CustomUser(email=validate['email'],
                                      name=validate['name'],
                                      uid=validate['uid'],
                                      image=validate['image']
                                      )

                    user.save()

                    data = {
                        "id": user.id,
                        "email": user.email,
                        "name": user.name,
                        "image": user.image,
                        "type": "new_user",
                        "provider": validate['provider']
                    }

                    self.response_format["data"] = data
                    self.response_format["status_code"] = status.HTTP_201_CREATED
                    self.response_format["error"] = None
                    self.response_format["message"] = "User Created Successfully"

            else:
                self.response_format["data"] = None
                self.response_format["status_code"] = status.HTTP_401_UNAUTHORIZED
                self.response_format["error"] = "Invalid token"
                self.response_format["message"] = "Invalid token"

        else:
            self.response_format["data"] = None
            self.response_format["status_code"] = status.HTTP_400_BAD_REQUEST
            self.response_format["error"] = "Token not provided"
            self.response_format["message"] = "Token not provided"

        return Response(self.response_format)
