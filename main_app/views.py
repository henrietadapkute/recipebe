from django.contrib.auth.models import Group, User
from .models import *
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, parsers
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, GroupSerializer, RecipeSerializer, CategorySerializer, PhotoSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = [permissions.IsAuthenticated]

class HomeView(APIView):
   permission_classes = (IsAuthenticated, )
   def get(self, request):
       content = {'message': 'hello'}
       return Response(content)


class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class SignupView(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        
        try:
            new_user = User.objects.create(username=username, email=email)
            new_user.set_password(password)
            new_user.save()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class PhotoViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    http_method_names = ['get', 'post', 'patch', 'delete']

class RecipeViewSet(viewsets.ModelViewSet):
    # queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    # permission_classes = [permissions.IsAuthenticated]
   
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        """
        Optionally filters recipes by category name provided in the query string.
        """
        queryset = Recipe.objects.all()
        category_name = self.request.query_params.get('category', None)
        if category_name is not None:
            category = get_object_or_404(Category, name=category_name)
            queryset = queryset.filter(category=category)
        return queryset

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['get'])
    def recipes(self, request, pk=None):
        category = self.get_object()
        recipes = Recipe.objects.filter(category=category)
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)
