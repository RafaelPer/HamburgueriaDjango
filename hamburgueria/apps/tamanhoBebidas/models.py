from django.db import models

# Create your models here.
class tamanhoBebida(models.Model):

    STATUS = (
        ('yes', 'sim'),
        ('no', 'não')
    )

    idTamanhoBebida = models.AutoField(primary_key = True)
    nome = models.CharField(max_length = 100, blank = False, null = False)
    descricao = models.TextField(blank = False, null = False, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "tamanhoBebida"
        verbose_name_plural = "tamanhosBebidas"
        ordering = ['nome']

    def __str__(self):
        return self.nome