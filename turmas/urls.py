from django.urls import path
from .views import TurmaList, TurmaDetail, TurmaCreate, AlunoCreate, AlunoUpdate

urlpatterns = [
    path('', TurmaList.as_view(), name='turma-list'),
    path('<int:pk>/', TurmaDetail.as_view(), name='turma-detail'),
    path('add/', TurmaCreate.as_view(), name='turma-add'),
    path('<int:turma_pk>/alunos/add/', AlunoCreate.as_view(), name='aluno-add'),
    path('alunos/<int:pk>/edit/', AlunoUpdate.as_view(), name='aluno-edit'),
]
