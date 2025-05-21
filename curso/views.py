from django.shortcuts import render
from .models import Curso, Aluno

# Create your views here.
def index(request):
    cursos = Curso.objects.all() # Select do django
    contexto = {
        'cursos': cursos,
    }
    return render(request, 'curso/index.html',contexto)

def alunos_do_curso(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    alunos = Aluno.objects.filter(curso=curso)
    return render(request, 'curso/alunos_do_curso.html', {'curso': curso, 'alunos': alunos})