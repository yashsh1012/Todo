from rest_framework import serializers
from .models import CustomUser, TAG, Todo
from django.db import models
from django.utils.translation import gettext_lazy as _
from drf_writable_nested import  WritableNestedModelSerializer




class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']

    def create(self,validated_data):
        user = CustomUser.objects.create(email = validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user    



class GetProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class UpdateProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['name', 'profil_pic']        



#------Merging 2 model serializers(TAG & Todo)
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TAG
        fields = ['tags']


class TodoSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    tag_name = TagSerializer(many=True)  #name should be the name of the field having many to many realtionship
    class Meta:
        model = Todo
       # fields = ['id' ,'Title', 'Description', 'Due_date', 'status', 'Created_Date' , 'Updated_Date', 'tag_name']
        fields = ['Title', 'Description', 'Due_date', 'status', 'Created_Date' , 'Updated_Date', 'tag_name']
#----------------------------------------------------

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TAG
        fields = ['tags']

class CreateTodoSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    tag_name = TagSerializer(many=True)  #name should be the name of the field having many to many realtionship
    class Meta:
        model = Todo
        fields = ['Title', 'Description', 'Due_date', 'status',  'tag_name']
