from django.db import models
from django.urls import reverse

class Cliente(models.Model):
    nome        = models.CharField(max_length=200)
    cpf         = models.CharField(max_length=11)
    idade       = models.IntegerField()
    email       = models.CharField(max_length=200)
    senha       = models.CharField(max_length=200)
    logradouro  = models.CharField(max_length=200)
    numero      = models.CharField(max_length=200)
    complemento = models.CharField(max_length=200)
    bairro      = models.CharField(max_length=200)
    cidade      = models.CharField(max_length=200)
    estado      = models.CharField(max_length=200)
    

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('cliente_edit', kwargs={'pk': self.pk})
