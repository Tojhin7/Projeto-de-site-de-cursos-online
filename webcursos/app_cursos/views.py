from django.shortcuts import render
from .models import Cursos
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    return render(request, 'app_cursos/home.html')

def logout_view(request):
    logout(request)
    return render(request, 'app_cursos/home.html')

class CursosListView(LoginRequiredMixin, ListView):
    model = Cursos #Por padrão a listview procura por um template chamado cursos_list.html

class CursosCreateView(CreateView): #O createview exige os 'fields' para saber quais campos o usuário irá preencher durante o cadastro
    model = Cursos
    fields = ['title', 'description'] #Quais campos o usuário irá preencher durante o cadastro. Ele também cria uma classe de formulário para o template, que por padrão é chamada de 'form' e pode ser acessada no template para renderizar os campos do formulário
    success_url = reverse_lazy('cursos_list') #Redireciona para a página de listagem de cursos após o cadastro de um novo curso. O reverse_lazy é usado para evitar problemas de importação circular, já que as URLs ainda não foram carregadas quando a classe é definida.

class CursosUpdateView(UpdateView):
    model = Cursos 
    fields = ['title', 'description']
    success_url = reverse_lazy('cursos_list')
    #Procuta um 'Curso' específico para atualizar. Podemos fazer isso através do Id do curso, que é passado na URL. O UpdateView espera que a URL tenha um parâmetro chamado 'pk' (primary key) para identificar qual curso deve ser atualizado. Por exemplo, a URL para atualizar um curso com id 1 seria algo como '/cursos/update/1/'. O UpdateView então usa esse 'pk' para buscar o curso correspondente no banco de dados e exibir o formulário de atualização com os dados atuais do curso preenchidos.

class CursosDeleteView(DeleteView):
    model = Cursos
    '''
        Assim como o UpdateView, o DeleteView envia pro contexto do template um object, ou o proprio nome do modelo 'cursos' em letras minusculas.
    '''
    success_url = reverse_lazy('cursos_list')