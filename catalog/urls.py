
from django.urls import path

from catalog.views import home, contacts, category_product

urlpatterns = [
    path('', home),
    path('contacts/', contacts),
    path('category_product/', category_product),
    path('contacts/', contacts, name="contacts"),

]