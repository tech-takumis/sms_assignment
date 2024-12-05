from django.urls import path
from .views import get_user,create_user, create_sms

urlpatterns = [
    path('users/',get_user, name="get_users"),
    path('users/create/',create_user, name="create_user"),
    path('sms/create',create_sms, name="create_sms"),
]
