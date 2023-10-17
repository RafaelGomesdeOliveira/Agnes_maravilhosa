from django.shortcuts import render

from django.http import HttpResponse


def create(request):
    return HttpResponse("Ola, aqui cria")

def list(request):
    return HttpResponse("Ola, aqui lista")

def delete(request):
    return HttpResponse("Ola, aqui apaga")

def update(request):
    return HttpResponse("Ola, aqui atualiza")


