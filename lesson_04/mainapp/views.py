from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from django.template.loader import render_to_string

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

    return render(request, 'mainapp/index.html', content)


def product_create(request):
    title = 'Добавление товара'
    data = dict()
    if request.method == 'POST':
        create_form = ProductCreateForm(request.POST)

        if create_form.is_valid():
            create_form.save()
            data['form_is_valid'] = True
            products = get_products()
            data['products_html'] = render_to_string(
                'mainapp/products_list.html', {'products': products})
        else:
            data['form_html'] = render_to_string(
                'mainapp/product_create.html',
                {'form': create_form},
                request=request)
    else:
        data['form_is_valid'] = False
        data['form_html'] = render_to_string('mainapp/product_create.html',
                                             {'form': ProductCreateForm()},
                                             request=request)
    return JsonResponse(data)
