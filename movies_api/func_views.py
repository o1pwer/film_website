from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


@api_view(['POST'])
def obtain_auth_token(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        if user := authenticate(username=username, password=password):
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    if request.method == 'POST':
        try:
            # Get the user's token and delete it
            user_token = Token.objects.get(user=request.user)
            user_token.delete()
            return Response({'detail': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({'detail': 'No token found for the user.'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        try:
            User.objects.create_user(username=username, password=password, email=email)
            return Response({'detail': 'User registered successfully.'}, status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response({'detail': 'Username or email already in use.'}, status=status.HTTP_400_BAD_REQUEST)
