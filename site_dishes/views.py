from django.shortcuts import render
from .models import Category, Recipe
from .form import RecipeForm


def index(request):
    recipes = []
    for item in Recipe.objects.all():
        recipes.append(item)
    category = Category.objects.all()
    context = {
        'result': recipes,
        'category': category
    }
    return render(request, 'index.html', context=context)


def recipe_add(request):
    title = 'Добавить рецепт'
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        message = 'Ошибка в данных'
        if request.user.is_authenticated:
            user = request.user
            if form.is_valid():
                title = form.cleaned_data['title']
                description = form.cleaned_data['description']
                ingredients = form.cleaned_data['ingredients']
                steps = form.cleaned_data['steps']
                time = form.cleaned_data['time']
                portions = form.cleaned_data['portions']
                image = form.cleaned_data['image']
                category = form.cleaned_data['category']
                recipe = Recipe(title=title,
                                description=description,
                                steps=steps,
                                ingredients=ingredients,
                                time=time,
                                portions=portions,
                                image=image,
                                author=user,
                                category=category)
                
                recipe.save()
                message = 'Рецепт сохранен'
        else:
            message = 'Добавлять рецепты могут только авторизованные пользователи'
    else:
        form = RecipeForm()
        message = 'Заполните форму'
    return render(request, 'form.html', {'form': form, 'message': message, 'title': title})


def recipe_view(request, recipe_id: int):
    recipe = Recipe.objects.filter(pk=recipe_id).first()
    context = {
        'result': recipe
        }
    return render(request, 'recipe.html', context=context)


def recipe_find(request):
    search = request.GET.get('search')
    result = []
    for item in Recipe.objects.all():
        if search.lower() in item.title.lower():
            result.append(item)
    context = {
        'result': result
    }
    return render(request, 'index.html', context=context)


def category_view(request, category: str):
    result = [] 
    for item in Recipe.objects.all():
        if category in item.category.title:
            result.append(item)
    category = Category.objects.all()
    context = {
        'result': result,
        'category': category
        }
    return render(request, 'index.html', context=context)


def author_view(request, username: str):
    result = [] 
    for item in Recipe.objects.all():
        if username in item.author.username:
            result.append(item)
    category = Category.objects.all()
    context = {
        'result': result,
        'category': category
        }
    return render(request, 'index.html', context=context)


