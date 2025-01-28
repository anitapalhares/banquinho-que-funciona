from django.urls import path

from . import views

urlpatterns = [
    path('ver_produto/', views.ver_produto, name='ver_produto'),
]

# urlpatterns = [
#     path('inserir_produto/', views.inserir_produto, name='inserir_produto'),
# ]


