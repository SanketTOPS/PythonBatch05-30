from django.shortcuts import render
from .serializers import studSerializer
from .models import studinfo
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def getalldata(request):
    if request.method=='GET':
        stobj=studinfo.objects.all()
        serial=studSerializer(stobj,many=True)
        return Response(serial.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getstid(request,id):
    if request.method=='GET':
        try:
            stid=studinfo.objects.get(id=id)
        except studinfo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serial=studSerializer(stid)
        return Response(serial.data,status=status.HTTP_202_ACCEPTED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deletedata(request,id):
    if request.method=='DELETE':
        try:
            stid=studinfo.objects.get(id=id)
        except studinfo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        studinfo.delete(stid)
        return Response(status=status.HTTP_202_ACCEPTED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

