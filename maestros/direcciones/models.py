from django.db import models
from django.utils.translation import gettext as _
from maestros.ciudades.models import Ciudad
from maestros.personas.models import Persona
from maestros.miscelaneosdet.models import DetMiscelaneo


ESTADO_ACTIVO  = 1
ESTADO_INACTIVO = 0

ESTADO_CHOICES = {
    (ESTADO_ACTIVO, _('Activo')),
    (ESTADO_INACTIVO, _('Inactivo')),
}

class Direccion(models.Model):
    id_persona = models.ForeignKey(Persona,on_delete=models.CASCADE)
    direccion_secuencia = models.CharField(max_length=4)
    direccion = models.CharField(max_length=400)
    referencia_direccion = models.CharField(max_length=200)
    telef_contacto = models.CharField(max_length=20)
    telefax = models.CharField(max_length=20)
    id_miscdet_tipodireccion = models.ForeignKey(DetMiscelaneo,on_delete=models.CASCADE,related_name='%(app_label)s_%(class)s_id_miscdet_edocivil')
    id_miscdet_situaciondomicilio = models.ForeignKey(DetMiscelaneo,on_delete=models.CASCADE,related_name='%(app_label)s_%(class)s_id_miscdet_nacionalidad')
    id_ciudad= models.ForeignKey(Ciudad,on_delete=models.CASCADE)
    es_cobranza = models.BooleanField(default=False)
    es_domicilio = models.BooleanField(default=False)
    es_remision = models.BooleanField(default=False)
    es_principal = models.BooleanField(default=False)
    es_otros = models.BooleanField(default=False)
    ind_estado  = models.PositiveSmallIntegerField(
        choices=ESTADO_CHOICES,
        default=ESTADO_ACTIVO
    )
    ult_usuario = models.CharField(max_length=100)
    ult_fecha  = models.DateTimeField(auto_now=True)
    ult_equipo = models.CharField(max_length = 200)
    ult_ip = models.GenericIPAddressField(null=True)

    def __str__(self):
        return self.direccion

    class Meta:
        db_table = "si_maestro_direcciones"
