from django import forms
from .models import Category, Recipe


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'steps', 'time', 'portions', 'image', 'category']