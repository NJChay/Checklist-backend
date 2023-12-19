import uuid

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from .models import TodoItem, User
from .serializers import DataSerializer, UserSerializer


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def check_owner():
    pass


def clean_id(data):
    data['id'] = str(uuid.uuid4())


@api_view(['GET'])
def getData(request):
    print(get_client_ip(request))
    app = TodoItem.objects.all()
    serializer = DataSerializer(app, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def postData(request):
    clean_id(request.data)
    print(request.data)
    serializer = DataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.errors)
    return Response(serializer.data)


@api_view(['POST'])
def loginUser(request):
    user = get_object_or_404(User, name=request.data['name'])
    serializer = UserSerializer(user)
    if not user.password == request.data['password']:
        return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['POST'])
def postUser(request):
    clean_id(request.data)
    print(request.data)
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(name=request.data['name'])
        user.password = hash(user.password)
        print(user.password)
        # token = Token.objects.create(user=user)
        return Response({"user": serializer.data})
    else:
        print(serializer.errors)
    return Response(serializer.data)


@api_view(['POST'])
def recoverUser(request):
    user = get_object_or_404(User, email=request.data['email'])
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def deleteData(request):
    print(request.GET.get('id'))
    TodoItem.objects.all().filter(id=request.GET.get('id')).delete()
    return Response()


@api_view(['PUT'])
def putData(request):
    clean_id(request.data)
    TodoItem.objects.all().filter(title=request.data.get('title')).delete()
    serializer = DataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.errors)
    return Response()


@api_view(['PUT'])
def updatePasword(request):
    user = get_object_or_404(User, email=request.data.get('email'))
    request.data['id'] = user.id
    request.data['name'] = user.name
    serializer = UserSerializer(data=request.data)
    User.objects.all().filter(email=request.data.get('email')).delete()
    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.errors)
    return Response()