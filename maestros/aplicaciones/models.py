from django.db import models
from django.utils.translation import gettext as _

ESTADO_ACTIVO  = 1
ESTADO_INACTIVO = 0
ESTADO_CHOICES = {
    (ESTADO_ACTIVO, _('Activo')),
    (ESTADO_INACTIVO, _('Inactivo')),
}

# Create your models here.
class Aplicacion(models.Model):
    cod_aplicacion = models.CharField(max_length = 4)
    nombre_aplicacion = models.CharField(max_length = 100)
    desc_aplicacion = models.CharField(max_length = 250)
    cod_dependencia = models.CharField(max_length = 4)
    ind_estado = models.PositiveSmallIntegerField(
        choices=ESTADO_CHOICES,
        default=ESTADO_ACTIVO
    )
    ult_usuario = models.CharField(max_length=100)
    ult_fecha  = models.DateTimeField(auto_now=True)
    ult_equipo = models.CharField(max_length = 200)
    ult_ip = models.GenericIPAddressField(null=True)
    
    class Meta:
        db_table = "si_maestro_aplicaciones"

    
    def __str__(self):
        return self.nombre_aplicacion
