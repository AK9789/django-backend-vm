from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TppSerializer
from .models import Tpp

# Create your views here.
@api_view(['POST'])
def createUser(request):
    serializer = TppSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def showAll(request):
    users = Tpp.objects.all()
    serializer = TppSerializer(users, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def userSpecific(request, pk):
    user = Tpp.objects.get(u_id=pk)
    serializer = TppSerializer(user, many=False)
    return Response(serializer.data)
