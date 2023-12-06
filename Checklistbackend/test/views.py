import uuid
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import TodoItem
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
def postUser(request):
    clean_id(request.data)
    print(request.data)
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.errors)
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteData(request):
    print(request.GET.get('id'))
    TodoItem.objects.all().filter(id=request.GET.get('id')).delete()
    return Response()


@api_view(['PUT'])
def putData(request):
    TodoItem.objects.all().filter(id=request.data.get('id')).delete()
    serializer = DataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.errors)
    return Response()
