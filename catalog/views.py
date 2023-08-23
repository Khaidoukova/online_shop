
from django.shortcuts import render
from django.urls import reverse_lazy

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


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


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    #fields = ('name', 'description', 'category', 'price', 'preview')
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    # fields = ('name', 'description', 'category', 'price', 'preview')
    success_url = reverse_lazy('catalog:product_form')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')




