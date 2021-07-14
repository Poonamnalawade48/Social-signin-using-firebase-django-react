from django.urls import path

from authentication.views import SocialSignupAPIView

urlpatterns = [
    path('socialSignup', SocialSignupAPIView.as_view(), name="social-signup"),
]