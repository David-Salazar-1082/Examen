from django.urls import path
from producto_app import views

urlpatterns = [
    path('',views.index_vista, name='views.index_vista')
]
