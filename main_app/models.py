from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='recipes', on_delete=models.CASCADE)
    description = models.TextField()
    prep_time = models.IntegerField(help_text='Preparation time in minutes')
    cook_time = models.IntegerField(help_text='Cooking time in minutes')
    servings = models.IntegerField(help_text='Number of servings')
    instructions = models.TextField()

    def __str__(self):
        return self.title


class Photo(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='photos')
  title = models.CharField(max_length=255)
  document = models.FileField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='photos', null=True, blank=True)
 
  class Meta:
    verbose_name_plural = 'Photos'

  def __str__(self):
    return f"Photo url: {self.url}"