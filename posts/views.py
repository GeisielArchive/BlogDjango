from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView


# Create your views here.
class PostIndex(ListView):
    ...


class PostBusca(PostIndex):
    ...


class PostCategoria(PostIndex):
    ...


class PostDetalhes(UpdateView):
    ...
