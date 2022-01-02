from django.db import models


class Setor(models.Model):
    nome = models.CharField(max_length=500)
    responsavel = models.CharField(max_length=500, blank=True, null=True)
    telefone = models.CharField(max_length=500, blank=True, null=True)
    descricao = models.CharField(max_length=3000, blank=True, null=True)
    secretaria_imediata = models.IntegerField(blank=True, null=True)
    setor_imediato = models.IntegerField(blank=True, null=True)
    nivel_hierarquia = models.IntegerField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Setor"
        verbose_name_plural = "Setores"

