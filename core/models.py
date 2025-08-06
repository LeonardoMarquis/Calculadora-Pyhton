from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=9)
    estoque = models.IntegerField('Estoque')

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    email = models.EmailField('Email', max_length=100)