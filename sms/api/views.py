from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer, MessageSerializer
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@api_view(['GET'])
def get_user(request):
    users = User.objects.all()
    serialize = UserSerializer(users, many=True)
    return Response(serialize.data)

@csrf_exempt
@api_view(['POST'])
def create_user(request):
    # first we need to to serialize the data
    serialize = UserSerializer(data=request.data)

    if serialize.is_valid():
        serialize.save()
        return Response(serialize.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['POST'])
def create_sms(request):
    print(f"Request data: {request.data}")  # Debug log
    serialize = MessageSerializer(data=request.data)

    if serialize.is_valid():
        try:
            serialize.save()
            print("Message saved successfully!")  # Debug log
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(f"Error during save: {e}")  # Debug log
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    print(f"Serializer errors: {serialize.errors}")  # Debug log
    return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
