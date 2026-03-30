from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from .models import Usuario

# Create your views here.

class InicioView(TemplateView):
    template_name = 'wallet/inicio.html'


class UsuarioListView(ListView):
    model = Usuario
    template_name = 'wallet/usuario_list.html'
    context_object_name = 'usuarios'


class UsuarioCreateView(CreateView):
    model = Usuario
    fields = ['nombre', 'correo', 'saldo']
    template_name = 'wallet/usuario_form.html'
    success_url = reverse_lazy('usuario_list')


class UsuarioUpdateView(UpdateView):
    model = Usuario
    fields = ['nombre', 'correo', 'saldo']
    template_name = 'wallet/usuario_form.html'
    success_url = reverse_lazy('usuario_list')


class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = 'wallet/usuario_confirm_delete.html'
    success_url = reverse_lazy('usuario_list')