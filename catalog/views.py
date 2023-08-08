from django.shortcuts import render
from catalog.models import Product

def home(request):
    index_list = Product.objects.all()
    context = {
        'object_list': index_list,
        'title': 'SkyStore'

    }
    return render(request, 'catalog/home.html', context)


def product(request):
    index_list = Product.objects.all()
    context = {
        'object_list': index_list,
        'title': 'Карточка товара'
    }
    return render(request, 'catalog/product.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')
        print(f"Имя: {name}, Телефон: {phone_number}, Сообщение: {message}")
    context = {
        'title': 'Контакты',
    }

    return render(request, 'catalog/contacts.html', context)



