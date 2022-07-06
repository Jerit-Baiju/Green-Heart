from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='admin-home'),
    path('add_product/', views.add_product, name='add-product'),
    path('add_pack/', views.add_pack, name='add-pack'),
    path('add_category/', views.add_category, name='add-category'),
    path('categories/', views.categories, name='categories'),
]
