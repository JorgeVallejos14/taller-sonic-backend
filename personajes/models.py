from django.db import models

# Create your models here.
class Personaje(models.Model):
    nombre = models.CharField(max_length=80,unique=True)
    poder = models.CharField(max_length=60)
    especial = models.PositiveSmallIntegerField(default=1)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    catalogo = models.ForeignKey(
        Personaje,
        on_delete=models.PROTECT,
        related_name='productos'
    )
    nombre = models.CharField(max_length=80)
    especie = models.CharField(max_length=60)
    descripcion = models.TextField(blank=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre()