from django.db import models

# Create your models here.

class ListaPresentes(models.Model):
    nome_do_item = models.CharField(max_length=255)
    quantidade = models.PositiveIntegerField()
    primeiro_nome = models.CharField(max_length=50)
    ultimo_nome = models.CharField(max_length=50)