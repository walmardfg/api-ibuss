from django.db import models
from maestros.aplicaciones.models import Aplicacion
from django.utils.translation import gettext as _

ESTADO_ACTIVO  = 1
ESTADO_INACTIVO = 0
ESTADO_CHOICES = {
    (ESTADO_ACTIVO, _('Activo')),
    (ESTADO_INACTIVO, _('Inactivo')),
}

# Create your models here.
class   Miscelaneo(models.Model):
    id_aplicacion = models.ForeignKey(Aplicacion,on_delete=models.CASCADE)
    cod_maestro  =  models.CharField(max_length=12,null=False, unique=True)
    nombre_maestro = models.CharField(max_length=100,null=False)
    desc_maestro  = models.CharField(max_length=150,null=True)
    ind_estado = models.PositiveSmallIntegerField(
        choices=ESTADO_CHOICES,
        default=ESTADO_ACTIVO
    )
    ult_usuario = models.CharField(max_length=100)
    ult_fecha  = models.DateTimeField(auto_now=True)
    ult_equipo = models.CharField(max_length = 200)
    ult_ip = models.GenericIPAddressField(null=True)
   
    class Meta:
        db_table = "si_maestro_miscelaneos"

    
    def __str__(self):
        return self.nombre_maestro
