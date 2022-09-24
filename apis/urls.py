from operator import imod
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('create/', views.create, name="create"),
    path('addvarient/', views.addvarient, name="addvarient"),
    path('singleproductdetals/<str:name>', views.singleproduct, name="singleproduct"),
    path('deleteproduct/<str:name>', views.delete_product, name="delete_product"),
    path('deletevariant/<str:name>/<str:title>', views.delete_variant, name="delete_variant"),
    path('listall/', views.listall, name="listall"),
    path('update/<str:name>', views.update, name="update"),

]