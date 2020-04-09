#     created_by  = models.ForeignKey(User, on_delete=models.CASCADE)
from django.db import models
from django.utils.translation import gettext as _
from maestros.personas.models import Persona

ESTADO_ACTIVO  = 1
ESTADO_INACTIVO = 0

ESTADO_CHOICES = {
    (ESTADO_ACTIVO, _('Activo')),
    (ESTADO_INACTIVO, _('Inactivo')),
}

class Compania(models.Model):
    cod_compania = models.CharField(max_length=20,unique=True)
    doc_fiscal = models.CharField(max_length=20,unique=True)
    pagina_web = models.CharField(max_length=200)
    desc_compania = models.CharField(max_length=250)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    telef_contact_1 = models.CharField(max_length=20)
    telef_contact_2 = models.CharField(max_length=20)
    telef_fax = models.CharField(max_length=20)
    telef_movil = models.CharField(max_length=20)
    logo_compania = models.ImageField(upload_to='companias')
    direccion = models.CharField(max_length=250)
    tipo_compania = models.CharField(max_length=2)
    certificado_reg = models.CharField(max_length=200)
    email_corp = models.CharField(max_length=20)
    id_persona_jefe = models.ForeignKey(Persona,on_delete=models.CASCADE,related_name='%(app_label)s_%(class)s_id_persona_jefe')
    id_persona_resp = models.ForeignKey(Persona,on_delete=models.CASCADE,related_name='%(app_label)s_%(class)s_id_persona_resp')
    ind_estado  = models.PositiveSmallIntegerField(
        choices=ESTADO_CHOICES,
        default=ESTADO_ACTIVO
    )
    ult_usuario = models.CharField(max_length=100)
    ult_fecha  = models.DateTimeField(auto_now=True)
    ult_equipo = models.CharField(max_length = 200)
    ult_ip = models.GenericIPAddressField(null=True)

    def __str__(self):
        return self.desc_compania

    class Meta:
        db_table = "si_maestro_companias"
