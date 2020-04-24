from django.db import models
from django.utils.translation import gettext as _
from maestros.monedas.models import Moneda


ESTADO_ACTIVO  = 1
ESTADO_INACTIVO = 0

ESTADO_CHOICES = {
    (ESTADO_ACTIVO, _('Activo')),
    (ESTADO_INACTIVO, _('Inactivo')),
}

class TipoCambio(models.Model):
    id_moneda_origen = models.ForeignKey(Moneda,on_delete=models.CASCADE)
    id_moneda_destino = models.ForeignKey(Moneda,on_delete=models.CASCADE,related_name='%(app_label)s_%(class)s_id_moneda_destino')
    fecha_cambio = models.DateTimeField(auto_now_add=True)
    factor_compra = models.DecimalField(max_digits=16, decimal_places=8)
    factor_venta = models.DecimalField(max_digits=16, decimal_places=8)
    factor_promedio = models.DecimalField(max_digits=16, decimal_places=8)
    ind_estado  = models.PositiveSmallIntegerField(
        choices=ESTADO_CHOICES,
        default=ESTADO_ACTIVO
    )
    ult_usuario = models.CharField(max_length=100)
    ult_fecha  = models.DateTimeField(auto_now=True)
    ult_equipo = models.CharField(max_length = 200)
    ult_ip = models.GenericIPAddressField(null=True)

    def __str__(self):
        return self.nombre_completo

    class Meta:
        db_table = "si_maestro_tipocambios"
