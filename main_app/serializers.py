from django.contrib.auth.models import Group, User 
from .models import Recipe, Category, Ingredient, RecipeIngredient
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User 
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['url', 'name', 'description']

class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['url', 'name', 'description']

class RecipeIngredientSerializer(serializers.HyperlinkedModelSerializer):
    ingredient_name = serializers.ReadOnlyField(source='ingredient.name')
    recipe_title = serializers.ReadOnlyField(source='recipe.title')

    class Meta:
        model = RecipeIngredient
        fields = ['url', 'recipe', 'recipe_title', 'ingredient', 'ingredient_name', 'quantity']
