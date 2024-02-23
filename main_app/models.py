from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='recipes', on_delete=models.CASCADE)
    description = models.TextField()
    prep_time = models.IntegerField(help_text='Preparation time in minutes')
    cook_time = models.IntegerField(help_text='Cooking time in minutes')
    servings = models.IntegerField(help_text='Number of servings')
    instructions = models.TextField()
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')

    def __str__(self):
        return self.title

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.quantity} of {self.ingredient.name} for {self.recipe.title}"

