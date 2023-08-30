from itertools import product

from django.urls import path

from catalog.views import home, contacts, category_product, create_product, categories, product, products

from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', home),
    path('contacts/', contacts, name="contacts"),
    path('categories/', categories, name='categories'),
    path('category_product/<int:pk>', category_product, name="category_product"),
    path('create_product/', create_product, name='create_product'),
    path('product/<int:pk>', product, name='product'),
    path('products/', products, name='products'),

]