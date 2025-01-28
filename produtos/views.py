from django.shortcuts import render
from django.http import HttpResponse
from.models import Pessoa
# Create your views here.

def ver_produto(request):
    if request.method == 'GET':
        nome = 'caio'
        return render(request, 'ver_produto.html', {'nome': nome})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')

        pessoa = Pessoa.objects.create(nome=nome, idade=idade)
        pessoa.save()

        pessoas = Pessoa.objects.all()
        print(pessoas)

        return render(request, 'ver_produto.html', {'produto': nome})


def inserir_produto(request):
    return render(request, 'inserir_produto.html')
