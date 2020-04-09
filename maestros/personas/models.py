from django.db import models
from django.utils.translation import gettext as _
from maestros.ciudades.models import Ciudad
from maestros.miscelaneosdet.models import DetMiscelaneo


ESTADO_ACTIVO  = 1
ESTADO_INACTIVO = 0

ESTADO_CHOICES = {
    (ESTADO_ACTIVO, _('Activo')),
    (ESTADO_INACTIVO, _('Inactivo')),
}

class Persona(models.Model):
    doc_identidad = models.CharField(max_length=12,unique=True)
    doc_fiscal = models.CharField(max_length=20)
    clase_persona = models.CharField(max_length=1)
    primer_apellido = models.CharField(max_length=100)
    segundo_apellido = models.CharField(max_length=100, null=True)
    primer_nombre = models.CharField(max_length=100)
    segundo_nombre = models.CharField(max_length=100, null=True)
    nombre_completo = models.CharField(max_length=100)
    nombre_busqueda = models.CharField(max_length=100)
    fecha_nacimiento = models.DateTimeField(auto_now_add=True)
    fecha_edocivil = models.DateTimeField(auto_now_add=True)
    telefono1 = models.CharField(max_length=20)
    telefono2 = models.CharField(max_length=20, null=True)
    telefax1  = models.CharField(max_length=20, null=True)
    email = models.EmailField()
    id_ciudad_nacimiento = models.ForeignKey(Ciudad,on_delete=models.CASCADE)
    id_miscdet_edocivil = models.ForeignKey(DetMiscelaneo,on_delete=models.CASCADE,related_name='%(app_label)s_%(class)s_id_miscdet_edocivil')
    id_miscdet_nacionalidad = models.ForeignKey(DetMiscelaneo,on_delete=models.CASCADE,related_name='%(app_label)s_%(class)s_id_miscdet_nacionalidad')
    id_miscdet_sexo = models.ForeignKey(DetMiscelaneo,on_delete=models.CASCADE,related_name='%(app_label)s_%(class)s_id_miscdet_sexo')
    es_cliente= models.BooleanField(default=False)
    es_proveedor = models.BooleanField(default=False)
    es_empleado = models.BooleanField(default=False)
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
        return self.nombre_completo

    class Meta:
        db_table = "si_maestro_personas"
