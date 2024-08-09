from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Post

def my_view(request):
    # Предположим, у нас есть список объектов, который мы хотим отпагировать
    objects_list = Post.objects.all()

    # Получаем параметр, который пользователь выбрал для количества элементов на странице
    page_size = request.GET.get('page_size')
    if not page_size:
        # Если параметр отсутствует, используем значение по умолчанию
        page_size = 10

    # Создаем объект Paginator с нашим списком объектов и количеством элементов на странице
    paginator = Paginator(objects_list, int(page_size))
    page_number = request.GET.get('page')
    if page_number is not None:
    # Преобразование page_number в целое число
        page_number = int(page_number)
    else:
    # Если страница не задана, используем первую страницу
        page_number = 1  

    # Проверяем, существует ли такая страница
    try:
        objects = paginator.page(page_number)
    except EmptyPage:
        # Если такой страницы нет, используем последнюю существующую
        objects = paginator.page(paginator.num_pages)

    # Теперь объекты содержит список объектов для текущей страницы
    context = {'objects': objects, 'page_size': page_size}

    # Возвращаем шаблон с переданным контекстом
    return render(request, 'my_template.html', context)