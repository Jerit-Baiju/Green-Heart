from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='admin-home'),
    path('add_product/', views.add_product, name='add-product'),
]
