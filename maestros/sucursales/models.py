from django.db import models
from django.utils.translation import gettext as _
from maestros.companias.models import Compania
from maestros.miscelaneosdet.models import DetMiscelaneo


ESTADO_ACTIVO  = 1
ESTADO_INACTIVO = 0

ESTADO_CHOICES = {
    (ESTADO_ACTIVO, _('Activo')),
    (ESTADO_INACTIVO, _('Inactivo')),
}

class Sucursal(models.Model):
    id_compania = models.ForeignKey(Compania,on_delete=models.CASCADE)
    desc_sucursal = models.CharField(max_length=200)
    direccion = models.CharField(max_length=500)
    telefono1 = models.CharField(max_length=20)
    telefono2 = models.CharField(max_length=20, null=True)
    telefax1  = models.CharField(max_length=20, null=True)
    email = models.EmailField()
    id_miscdet_gruposucursal = models.ForeignKey(DetMiscelaneo,on_delete=models.CASCADE)
    ind_estado  = models.PositiveSmallIntegerField(
        choices=ESTADO_CHOICES,
        default=ESTADO_ACTIVO
    )
    ult_usuario = models.CharField(max_length=100)
    ult_fecha  = models.DateTimeField(auto_now=True)
    ult_equipo = models.CharField(max_length = 200)
    ult_ip = models.GenericIPAddressField(null=True)

    def __str__(self):
        return self.desc_sucursal

    class Meta:
        db_table = "si_maestro_sucursales"
