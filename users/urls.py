from .views import UserCreateView, VerifyAPIView
from django.urls import path

urlpatterns = [
    path("user-create/", UserCreateView.as_view()),
    path('verify/', VerifyAPIView.as_view()),
    path('new-verify/', GetNewVerification.as_view()),
]

