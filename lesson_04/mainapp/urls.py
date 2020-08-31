from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.products_list,
         name='products'),
    path('create/',
         mainapp.product_create,
         name='product_create'),
]
