
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import TodoItem
from .serializers import DataSerializer


@api_view(['GET'])
def getData(request):
    app = TodoItem.objects.all()
    serializer = DataSerializer(app, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def postData(request):
    print(request.data)
    serializer = DataSerializer(data=request.data)
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
