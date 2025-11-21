from django.db import models

class ImagemItem(models.Model):
    item = models.ForeignKey(
        'ItemAcervo',
        on_delete=models.CASCADE,
        related_name='imagens'
    )

    imagem = models.ImageField(upload_to='itens_acervo/')
    legenda = models.CharField(max_length=255, blank=True, null=True)

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Imagem de {self.item.numero_acervo}"
