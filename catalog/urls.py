from itertools import product

from django.urls import path

from catalog.views import home, contacts, category_product


from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', home),
    path('contacts/', contacts, name="contacts"),
    path('category_product/', category_product, name="category_product"),

]