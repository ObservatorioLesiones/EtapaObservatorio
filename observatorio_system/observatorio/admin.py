from django.contrib import admin
from observatorio.models import evento
from observatorio.models import persona
from observatorio.models import vehiculo
from observatorio.models import Delegacion
from observatorio.models import Ciudad
from observatorio.models import Municipio
from observatorio.models import Condicion_Vial
from observatorio.models import Descripcion_Vial
from observatorio.models import num_carriles
from observatorio.models import dispositivo_funcionando
from observatorio.models import dispositivo_control_vial
from observatorio.models import condicion_luz
from observatorio.models import zona_construccion
from observatorio.models import condicion_atmosferica
from observatorio.models import metodo_transporte
from observatorio.models import jurisdiccion_especial


admin.site.register(evento)
admin.site.register(persona)
admin.site.register(vehiculo)

admin.site.register(Ciudad)
admin.site.register(Municipio)
admin.site.register(Delegacion)

admin.site.register(Condicion_Vial)
admin.site.register(Descripcion_Vial)
admin.site.register(num_carriles)

admin.site.register(dispositivo_funcionando)
admin.site.register(dispositivo_control_vial)
admin.site.register(condicion_luz)
admin.site.register(zona_construccion)

admin.site.register(condicion_atmosferica)
admin.site.register(metodo_transporte)
admin.site.register(jurisdiccion_especial)

