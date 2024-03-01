from django.contrib.auth.models import Group, User 
from .models import *
from .views import *
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User 
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class RecipeSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()

    def get_category_name(self, obj):
        return obj.category.name

    class Meta:
        model = Recipe
        fields = '__all__'


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['url', 'name', 'id']

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'