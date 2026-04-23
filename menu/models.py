from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome da Categoria")

    class Meta:
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=150, verbose_name="Nome do Café")
    description = models.TextField(verbose_name="Descrição")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Preço")
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="Foto")
    is_available = models.BooleanField(default=True, verbose_name="Disponível")

    def __str__(self):
        return self.name