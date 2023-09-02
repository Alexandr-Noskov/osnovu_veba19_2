from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogDeleteView, BlogDetailView, BlogListView, BlogUpdateView, BlogCreateView
from catalog.views import home, contacts
from config import settings
from django.conf.urls.static import static

app_name = BlogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog/list/', BlogListView.as_view(), name='blog_list'),
    path('blog/view/<int:pk>', BlogDetailView.as_view(), name='blog_view'),
    path('blog/edit/<int:pk>', BlogUpdateView.as_view(), name='blog_edit'),
    path('blog/delete/<int:pk>', BlogDeleteView.as_view(), name='blog_delete'),
]