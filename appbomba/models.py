from django.db import models

# Create your models here.


class CarroBomba(models.Model):
    patente = models.CharField(primary_key=True, max_length=6)
    marca = models.CharField(max_length=15)
    nomenclatura = models.CharField(max_length=5)
    cia = models.PositiveSmallIntegerField

    def __str__(self):
        texto = "{0} {1} {2}"
        return texto.format(self.patente, self.marca, self.nomenclatura)
    



