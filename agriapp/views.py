from django.shortcuts import render
from .models import UserLogin, HomePageData
from rest_framework import status
from rest_framework.viewsets import ViewSet
from .serializers import UserLoginAPI, HomePageAPI
from django.http import HttpResponse
from rest_framework.response import Response
# Create your views here.


class UserLoginView(ViewSet):
    def get(self, request):
        print(request.data)
        queryset = UserLogin.objects.all()
        serializer = UserLoginAPI(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        print(request.data)
        email = request.data['email']
        password = request.data['password']
        try:
            userData = UserLogin.objects.filter(email=email, password=password)
        except Exception as e:
            return Response({'msg':'user does not exist'}, status=status.HTTP_404_NOT_FOUND)
        # serializer = UserLoginAPI(data=request.data)
        if userData:
            return Response({'bool':True})
        else:
            return Response({'bool':False})
        
        
class HomePageView(ViewSet):
    def get(self, request):
        print(request.data)
        queryset = HomePageData.objects.all()
        serializer = HomePageAPI(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        