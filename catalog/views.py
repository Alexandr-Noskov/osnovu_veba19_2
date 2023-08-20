from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Category, Product


def home(request) -> HttpResponse:
    '''
    Контролер для главной страницы интернет-магазина
    :return: HTTP-ответ с отображением шаблона "home.html"
    '''
    return render(request, 'catalog/home.html')


def contacts(request) -> HttpResponse:
    '''
    Контролер для клиента интернет-магазина
    :return: HTTP-ответ с отображением шаблона "contacts.html"
    '''
    if request.method == 'POST':
        data = {}
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        data['user_1'] = (name, email, message)
        print(data)

    return render(request, 'catalog/contacts.html')

def category_product(request, pk):
    category_item = Category.objects.get(id=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': category_item.name,
        'description': category_item.description[:100]
    }
    return render(request, 'catalog/category_product.html', context)