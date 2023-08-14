from django.shortcuts import render
from django.urls import reverse_lazy

from catalog.models import Product
from django.views.generic import ListView, DetailView, CreateView


class ProductListView(ListView):
    model = Product



class ProductDetailView(DetailView):
    model = Product



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

#def add_product(request):
 #   product_to_add = []
  #  if request.method == 'POST':
   #     product = {
    #        'name': request.POST.get('name'),
     #       'description': request.POST.get('description'),
      #      'category': request.POST.get('category'),
       #     'price': request.POST.get('price'),
        #    'creation_date': request.POST.get('creation_date'),
         #   'change_date': request.POST.get('change_date')
#
 #       }
  #      product_to_add.append(Product(**product))
   #     Product.objects.bulk_create(product_to_add)
#
 #   return render(request, 'catalog/add_product.html')


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'category', 'price', 'preview')
    success_url = reverse_lazy('catalog:product_form')






