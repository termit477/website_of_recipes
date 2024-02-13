from django.contrib import admin
from .models import Category, Recipe

# Register your models here.

class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'time']
    ordering = ['title']
    list_filter = ['title']
    search_fields = ['title']
    search_help_text = 'Поиск по названию Рецепта'

    readonly_fields = ['author']

    fieldsets = [
        ('Рецпт',
         {
             'classes': ['wide'],
             'fields': ['title', 'description', 'author', 'category'],
         },
         ),
        ('Детали',
         {
             'classes': ['collapse'],
             'description': 'Описание рецепта',
             'fields': ['steps', 'ingredients', 'time', 'portions', 'image'],
         },
         ),
    ]

admin.site.register(Category)
admin.site.register(Recipe, RecipeAdmin)