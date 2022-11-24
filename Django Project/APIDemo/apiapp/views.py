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


@api_view(['POST'])
def savedata(request):
    if request.method=='POST':
        studserial=studSerializer(data=request.data)
        if studserial.is_valid():
            studserial.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def updatedata(request,id):
    try:
        uid=studinfo.objects.get(id=id)
        #serial=studSerializer(uid)
        #return Response(serial.data)
    except studinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='PUT':
        serial=studSerializer(uid,data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(data=serial.data,status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST) 
    
    



