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
from observatorio.models import tipo_incidente
from observatorio.models import rol_persona
from observatorio.models import gravedad_lesion
from observatorio.models import medidas_seguridad
from observatorio.models import muerte_escena
from observatorio.models import ocupacion
from observatorio.models import estado_civil
from observatorio.models import escolaridad
from observatorio.models import prioridad
from observatorio.models import tipo_licencia
from observatorio.models import conductor_alcoholizado
from observatorio.models import posicion_persona
from observatorio.models import tipo_accidente
from observatorio.models import interseccion_accidente
from observatorio.models import escenario_impacto
from observatorio.models import tipo_impacto
from observatorio.models import ubicacion_impacto
from observatorio.models import posicion_transeunte
from observatorio.models import direccion_inicial
from observatorio.models import conductor
from observatorio.models import pasajero
from observatorio.models import transeunte
from observatorio.models import marca
from observatorio.models import modelo
from observatorio.models import camion_pasajeros
from observatorio.models import volcadura



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

admin.site.register(marca)
admin.site.register(modelo)
admin.site.register(camion_pasajeros)
admin.site.register(volcadura)

admin.site.register(rol_persona)
admin.site.register(gravedad_lesion)
admin.site.register(medidas_seguridad)
admin.site.register(muerte_escena)
admin.site.register(ocupacion)
admin.site.register(estado_civil)
admin.site.register(escolaridad)
admin.site.register(prioridad)
admin.site.register(tipo_licencia)
admin.site.register(conductor_alcoholizado)
admin.site.register(posicion_persona)
admin.site.register(tipo_accidente)
admin.site.register(interseccion_accidente)
admin.site.register(escenario_impacto)
admin.site.register(tipo_impacto)
admin.site.register(ubicacion_impacto)
admin.site.register(posicion_transeunte)
admin.site.register(direccion_inicial)
admin.site.register(conductor)
admin.site.register(pasajero)
admin.site.register(transeunte)
admin.site.register(tipo_incidente)

