# from django.shortcuts import render
from django.http import HttpResponse


# Главная страница
def index(request):
    return HttpResponse('Главная страница')


# Страница со списком групп
'''def group_list(request):
    return HttpResponse('Список групп')'''


# Страница с информацией о постах отфильтрованных по группам;
# view-функция принимает параметр slug из path()
def group_posts(request, posts):
    return HttpResponse(f'Группа: {posts}')
