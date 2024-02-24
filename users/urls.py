from .views import UserCreateView, VerifyAPIView, GetNewVerification, ChangeUserInformationView, ChangeUserPhotoView
from django.urls import path

urlpatterns = [
    path("user-create", UserCreateView.as_view()),
    path('verify', VerifyAPIView.as_view()),
    path('new-verify', GetNewVerification.as_view()),
    path('change-info', ChangeUserInformationView.as_view()),
    path('add-photo', ChangeUserPhotoView.as_view()),
]

