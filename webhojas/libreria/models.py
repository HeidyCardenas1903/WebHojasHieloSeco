from django.db import models
from django.core.validators import RegexValidator


alpha_only_validator = RegexValidator(
    #Para asegurarse que en el campo nombre no se ingresen numeros 
    regex=r'^[a-zA-Z]*$',
    message='Este campo debe contener solo letras.',
)

# creacion de tbala ventas :)
class Ventas(models.Model):
    '''creacion tabla ventas'''
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(blank=False,null=False,max_length=40,validators=[alpha_only_validator])
    tipo_cliente=models.IntegerField(blank=False,null=False)
    cantidad=models.IntegerField(blank=False,null=False,default=0)
    precio_por_hoja=models.DecimalField(default=0.0, max_digits=8,decimal_places=2)
    subtotal=models.DecimalField(default=0.0, max_digits=8,decimal_places=2)
    neto_por_pagar=models.DecimalField(default=0.0, max_digits=8,decimal_places=2)

    def __str__(self):
        return self.nombre #Se define que el nombre del cliente es el que aparecera en los registros del admin.
    