from django.shortcuts import render, redirect
from .models import Pessoa

def inicial(request):
   return render(request, 'home.html')

def home(request):
   pessoa = Pessoa.objects.all()
   return render (request, 'index.html', {"pessoas": pessoa})

def salvar(request):
   nome = request.POST.get("nome")
   dt_nascimento = request.POST.get("dt_nascimento")
   Pessoa.objects.create(nome=nome, dt_nascimento=dt_nascimento)
   pessoa = Pessoa.objects.all()
   return render(request, "index.html", {"pessoas": pessoa})

def editar(request, id):
   pessoa = Pessoa.objects.get(id=id)
   return render(request, "update.html", {"pessoas": pessoa})

def update(request, id):
   nnome = request.POST.get("nome")
   dt_nascimento = request.POST.get("dt_nascimento")
   pessoa = Pessoa.objects.get(id=id)
   pessoa.nome = nnome
   pessoa.dt_nascimento = dt_nascimento
   pessoa.save()
   return redirect(home)

def delete(request, id):
   pessoa = Pessoa.objects.get(id=id)
   pessoa.delete()
   return redirect(home)