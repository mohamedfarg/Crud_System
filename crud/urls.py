from django.urls import path

from .views import *
urlpatterns = [
    path("home",all_products,name="home"),
    path("add",create_product,name="add"),
    path("edit/<int:id>",edit_product,name="edit"),
    path("delete/<int:id>",delete_product,name="delete"),
]