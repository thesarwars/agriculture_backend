from rest_framework import serializers
from .models import UserLogin, HomePageData


class UserLoginAPI(serializers.ModelSerializer):
    class Meta:
        model = UserLogin
        fields = '__all__'
        
        
class HomePageAPI(serializers.ModelSerializer):
    class Meta:
        model = HomePageData
        fields = '__all__'