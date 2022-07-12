from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('<str:category>/<str:pk>',views.product),
    path('<str:category>/<str:pk>/edit',views.edit_product),

]
