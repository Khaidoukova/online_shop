from django.shortcuts import render
from catalog.models import Product

def home(request):
    index_list = Product.objects.all()
    context = {
        'object_list': index_list
    }
    return render(request, 'catalog/home.html', context)


def index(request):
    index_list = Product.objects.all()
    context = {
        'object_list': index_list
    }
    return render(request, 'catalog/index.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')
        print(f"Имя: {name}, Телефон: {phone_number}, Сообщение: {message}")

    return render(request, 'catalog/contacts.html')



