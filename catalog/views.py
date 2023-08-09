from django.shortcuts import render, get_object_or_404
from catalog.models import Product

def home(request):
    index_list = Product.objects.all()
    context = {
        'object_list': index_list,
        'title': 'SkyStore'

    }
    return render(request, 'catalog/home.html', context)


def product(request, pk):
    product_info = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product.html', {'product': product_info})


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

def add_product(request):
    product_to_add = []
    if request.method == 'POST':
        product = {
            'name': request.POST.get('name'),
            'description': request.POST.get('description'),
            'category': request.POST.get('category'),
            'price': request.POST.get('price'),
            'creation_date': request.POST.get('creation_date'),
            'change_date': request.POST.get('change_date')

        }
        product_to_add.append(Product(**product))
        Product.objects.bulk_create(product_to_add)

    return render(request, 'catalog/add_product.html')









