#     created_by  = models.ForeignKey(User, on_delete=models.CASCADE)
from django.db import models
from django.utils.translation import gettext as _
from maestros.grupocentrocostos.models import GrupoCentroCosto

ESTADO_ACTIVO  = 1
ESTADO_INACTIVO = 0

ESTADO_CHOICES = {
    (ESTADO_ACTIVO, _('Activo')),
    (ESTADO_INACTIVO, _('Inactivo')),
}

class SubGrupoCentroCosto(models.Model):
    id_grupocentrocosto = models.ForeignKey(GrupoCentroCosto,on_delete= models.CASCADE)
    cod_subgrupo = models.CharField(max_length = 20, unique= True)
    desc_subgrupo = models.CharField(max_length = 200)
    ind_estado  = models.PositiveSmallIntegerField(
        choices=ESTADO_CHOICES,
        default=ESTADO_ACTIVO
    )
    ult_usuario = models.CharField(max_length=100)
    ult_fecha  = models.DateTimeField(auto_now=True)
    ult_equipo = models.CharField(max_length = 200)
    ult_ip = models.GenericIPAddressField(null=True)
    
    def __str__(self):
        return self.desc_subgrupo

    class Meta:
        db_table = "si_maestro_subgrupocentrocostos"
