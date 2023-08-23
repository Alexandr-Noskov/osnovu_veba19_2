from itertools import product

from django.urls import path

from catalog.views import home, contacts, category_product, create_product

from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', home),
    path('contacts/', contacts, name="contacts"),
    path('categories/', categories, name='categories'),
    path('category_product/', category_product, name="category_product"),
    path('create_product/', create_product, name='create_product'),
]