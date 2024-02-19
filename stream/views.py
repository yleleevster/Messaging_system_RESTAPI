from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import User, Message
from .serializers import UserSerializer, MessageSerializer
from rest_framework import status


@api_view(['GET'])
def all_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


@api_view(['GET', 'DELETE'])
def specific_user(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response("User not found!", status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        user.delete()
        return Response("The user has been deleted!", status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def messages(request):
    if request.method == 'GET':
        message = Message.objects.all()
        serializer = MessageSerializer(message, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:  
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def specific_message(request, message_id):
    try:
        message = Message.objects.get(pk=message_id)
    except Message.DoesNotExist:
        return Response("The message does not exist!",
                        status=status.HTTP_404_NOT_FOUND)
    if message.sender.id == request.user.id or message.receiver.id == request.user.id:
        if request.method == 'GET':
            message.is_read = True
            message.save()
            return Response(MessageSerializer(message).data, status=status.HTTP_200_OK)
        else:  # DELETE
            message.delete()
            return Response(MessageSerializer(message).data, status=status.HTTP_200_OK)
    return Response("You can't access messages that not belong to you!", status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def all_user_messages(request, user_id):
    if request.user.id == user_id:
        user_messages = Message.objects.filter(receiver=user_id)
        serializer = MessageSerializer(user_messages, many=True)
        return Response(serializer.data)
    return Response("You can't access messages that not belong to you!", status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def all_user_unread_messages(request, user_id):
    if request.user.id == user_id:
        user_messages = Message.objects.filter(receiver=user_id, is_read=False)
        serializer = MessageSerializer(user_messages, many=True)
        return Response(serializer.data)
    return Response("You can't access messages that not belong to you!", status=status.HTTP_401_UNAUTHORIZED)
