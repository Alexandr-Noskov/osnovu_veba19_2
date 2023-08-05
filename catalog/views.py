from django.http import HttpResponse
from django.shortcuts import render


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
