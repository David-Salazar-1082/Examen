from django.db import models

# Create your models here.

class products(models.Model):
    id_producto=models.CharField(primary_key=True,max_length=1000)
    nom_producto=models.CharField(max_length=30)
    tipo_prod=models.CharField(max_length=20)
    cant_prod=models.IntegerField()
    metodo_pag=models.CharField(max_length=10)
    proveedor_prod=models.CharField(max_length=20)
    id_proveedor=models.IntegerField()
    def __str__(self) -> str:
        return self.nom_producto