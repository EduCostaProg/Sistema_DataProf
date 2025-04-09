from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Turma, Aluno

class TurmaList(ListView):
    model = Turma
    template_name = 'turmas/turma_list.html'
    context_object_name = 'turmas'

class TurmaDetail(DetailView):
    model = Turma
    template_name = 'turmas/turma_detail.html'
    context_object_name = 'turma'

class TurmaCreate(CreateView):
    model = Turma
    fields = ['nome', 'descricao']
    template_name = 'turmas/turma_form.html'
    success_url = reverse_lazy('turma-list')

class AlunoCreate(CreateView):
    model = Aluno
    fields = ['nome', 'email', 'idade']
    template_name = 'turmas/aluno_form.html'
    
    def form_valid(self, form):
        # Obtem a turma com base no parâmetro da URL e a atribui ao aluno
        turma = Turma.objects.get(pk=self.kwargs['turma_pk'])
        form.instance.turma = turma
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adiciona a turma no contexto para o template usar (ex.: no link "Cancelar")
        context['turma'] = Turma.objects.get(pk=self.kwargs['turma_pk'])
        return context

    def get_success_url(self):
        # Após criar, usa a turma vinculada ao aluno recém-criado
        return reverse_lazy('turma-detail', kwargs={'pk': self.object.turma.pk})

class AlunoUpdate(UpdateView):
    model = Aluno
    fields = ['nome', 'email', 'idade']
    template_name = 'turmas/aluno_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Para edição, passa a turma associada ao aluno
        context['turma'] = self.object.turma
        return context

    def get_success_url(self):
        return reverse_lazy('turma-detail', kwargs={'pk': self.object.turma.pk})
