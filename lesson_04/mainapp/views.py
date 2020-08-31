from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from mainapp.models import Product
from mainapp.forms import ProductCreateForm


def get_products():
    products = Product.objects.all()
    return products


def products_list(request):
    title = 'Главная'
    products = get_products()

    content = {
        'title': title,
        'products': products
    }

    return render(request, 'mainapp/products_list.html', content)


def product_create(request):
    title = 'Добавление товара'
    if request.method == 'POST':
        create_form = ProductCreateForm(request.POST)

        if create_form.is_valid():
            create_form.save()
            return HttpResponseRedirect(reverse('mainapp:products'))
    else:
        create_form = ProductCreateForm()

    content = {
        'title': title,
        'create_form': create_form,
    }

    return render(request, 'mainapp/product_create.html', content)
