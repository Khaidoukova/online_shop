from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse

from catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from catalog.models import Product, Version
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            queryset = super().get_queryset()
        else:
            queryset = super().get_queryset().filter(status=Product.STATUS_PUBLISHED)

        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        for product in context_data['object_list']:
            active_version = Version.objects.filter(product=product, is_active=True).last()
            if active_version:
                product.active_version_number = active_version.version
                product.active_version_name = active_version.version_name
            else:
                product.active_version_number = None
                product.active_version_name = None
        return context_data


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
    success_url = reverse_lazy('catalog:product_form')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductModeratorForm
    success_url = reverse_lazy('catalog:home')
    permission_required = 'catalog.change_product'

    def test_func(self):
        user = self.request.user
        product = self.get_object()

        if product.owner == user or user.is_staff:
            return True
        else:
            return False


    def handle_no_permissions(self):
        return redirect(reverse_lazy('product_list'))


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')
    permission_required = 'catalog.delete_product'



