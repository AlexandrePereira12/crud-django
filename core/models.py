from django.db import models
from django.utils.timezone import now

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True)
    dt_nascimento = models.DateField()


    def __str__(self):
        return self.nome
    