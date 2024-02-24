from django.db import models

# Create your models here.
class InvitadosCasa(models.Model):
    nombre = models.CharField(max_length=50)
    carnet = models.CharField(max_length=50)
    placavehiculo= models.CharField(max_length=10)
    fecha = models.DateField()
    motivo = models.CharField(max_length=100)
    dueno_id = models.IntegerField()
    ingreso = models.IntegerField()
    def __str__(self):
        return self.nombre

class InvitadosAreaComun(models.Model):
    nombre = models.CharField(max_length=50)
    carnet = models.CharField(max_length=50)
    placaVehiculo = models.CharField(max_length=10, blank=True)
    fecha = models.DateField()
    areacomun_id = models.IntegerField()
    dueo_id = models.IntegerField()
    ingreso = models.IntegerField()
    def __str__(self):
        return self.nombre