from django.db import models

# Create your models here.

class Medico(models.Model):
    nome = models.CharField(max_length=100)
    e_mail = models.CharField(max_length=30)
    senha = models.CharField(max_length=20)
    data_de_criacao = models.DateTimeField(max_length=9)

    def __str__(self):
        return self.nome