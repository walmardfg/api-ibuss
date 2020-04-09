from django.db import models
from django.utils.translation import gettext as _
from maestros.municipios.models import Municipio

ESTADO_ACTIVO  = 1
ESTADO_INACTIVO = 0

ESTADO_CHOICES = {
    (ESTADO_ACTIVO, _('Activo')),
    (ESTADO_INACTIVO, _('Inactivo')),
}

class Parroquia(models.Model):
    id_municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    desc_parroquia = models.CharField(max_length = 255)
    ind_estado  = models.PositiveSmallIntegerField(
        choices=ESTADO_CHOICES,
        default=ESTADO_ACTIVO
    )
    ult_usuario = models.CharField(max_length=100)
    ult_fecha  = models.DateTimeField(auto_now=True)
    ult_equipo = models.CharField(max_length = 200)
    ult_ip = models.GenericIPAddressField(null=True)

    def __str__(self):
        return self.desc_parroquia

    class Meta:
        db_table = "si_maestro_parroquias"

