from django.urls import path
from .views import index, recipe_add, recipe_view, recipe_find, author_view, category_view

urlpatterns = [
    path('', index, name='index'),
    path('recipe_add/', recipe_add, name='recipe_add'),
    path('recipe/<int:recipe_id>', recipe_view, name='recipe_view'),
    path('search/', recipe_find, name='search'),
    path('category/<str:category>', category_view, name='category_view'),
    path('author/<str:username>', author_view, name='author_view'),
]