from django.db import models

# Create your models here.

class Municipio(models.Model):
	nombre_municipio=models.CharField(max_length=25)
	def __unicode__(self):
		return self.nombre_municipio

class Ciudad(models.Model):
	nombre_ciudad=models.CharField(max_length=25)
	municipio=models.ForeignKey(Municipio)
	def __unicode__(self):
		return self.nombre_ciudad

class Delegacion(models.Model):
	nombre_delegacion=models.CharField(max_length=25)
	municipio=models.ForeignKey(Municipio)
	def __unicode__(self):
		return self.nombre_d

class Condicion_Vial(models.Model):
	condicion_vial=models.CharField(max_length=30)

	def __unicode__(self):
		return self.condicion_vial

class Descripcion_Vial(models.Model):
	descripcion=models.CharField(max_length=55)

	def __unicode__(self):
		return self.descripcion


class num_carriles(models.Model):
	num_carriles=models.CharField(max_length=30)
	def __unicode__(self):
		return self.num_carriles

class dispositivo_funcionando(models.Model):
	funcionando=models.CharField(max_length=40)
	def __unicode__(self):
		return self.funcionando

class dispositivo_control_vial(models.Model):
	dispositivo_control=models.CharField(max_length=55)
	def __unicode__(self):
		return self.dispositivo_control


class condicion_luz(models.Model):
	condicion_luz=models.CharField(max_length=35)
	
	def __unicode__(self):
		return self.condicion_luz

class zona_construccion(models.Model):
	descripcion=models.CharField(max_length=35)

	def __unicode__(self):
		return self.descripcion

class condicion_atmosferica(models.Model):
	condicion=models.CharField(max_length=25)

	def __unicode__(self):
		return self.condicion

class metodo_transporte(models.Model):
	metodo=models.CharField(max_length=45)

	def __unicode__(self):
		return self.metodo

class jurisdiccion_especial(models.Model):
	jurisdiccion=models.CharField(max_length=25)

	def __unicode__(self):
		return self.jurisdiccion

class evento(models.Model):
	num_evento=models.AutoField(primary_key=True)
	delegacion=models.ForeignKey(Delegacion)
	ciudad=models.ForeignKey(Ciudad)
	municipio=models.ForeignKey(Municipio)
	latitud=models.DecimalField(max_digits=11, decimal_places=7, blank=True, default=0)
	longitud=models.DecimalField(max_digits=11, decimal_places=7, blank=True, default=0)
	descripcion_vial=models.ForeignKey(Descripcion_Vial)
	num_carriles=models.ForeignKey(num_carriles)
	limite_velocidad=models.IntegerField()
	condicion_vial=models.ForeignKey(Condicion_Vial)
	fecha_hora=models.DateTimeField('fecha incidente')
	jurisdiccion_especial=models.ForeignKey(jurisdiccion_especial)
	zona_construccion=models.ForeignKey(zona_construccion)
	condicion_luz=models.ForeignKey(condicion_luz)
	condicion_atmosfera=models.ForeignKey(condicion_atmosferica)
	hra_llamada=models.TimeField((u"Hora de llamada: "), blank=True)
	hra_escena=models.TimeField((u"Hora en la escena:"), blank=True)
	hra_hospital=models.TimeField((u"Hora en el hospital:"), blank=True)
	metodo_transportacion=models.ForeignKey(metodo_transporte)
	conductor_alcoholizado=models.IntegerField()
	num_lesionados=models.IntegerField()
	num_muertes=models.IntegerField()
	dispositivo_control_vial=models.ForeignKey(dispositivo_control_vial)
	dispositivo_funcionando=models.ForeignKey(dispositivo_funcionando)
	@models.permalink
	def get_absolute_url(self):
		return ('observatorio.views.ver_evento',(str(self.num_evento),),{})
	
	def __unicode__(self):
		return unicode(self.num_evento)

class marca(models.Model):
	marca=models.CharField(max_length=40)

	def __unicode__(self):
		return self.marca

class modelo(models.Model):
	marca=models.ForeignKey(marca)
	modelo=models.CharField(max_length=30)
	
	def __unicode__(self):
		return self.modelo

class camion_pasajeros(models.Model):
	tipo_camion=models.CharField(max_length=40)

	def __unicode__(self):
		return self.tipo_camion

class volcadura(models.Model):
	volcadura=models.CharField(max_length=45)

	def __unicode__(self):
		return self.volcadura

class vehiculo(models.Model):
	num_vehiculo=models.AutoField(primary_key=True)
	num_ocupantes=models.IntegerField()
	modelo=models.ForeignKey(modelo)
	marca=models.ForeignKey(marca)
	ano=models.IntegerField()
	vin=models.IntegerField()
	num_muertos=models.IntegerField()
	conductor_alcoholizado=models.BooleanField()
	num_lesionados=models.PositiveIntegerField()
	evento=models.ForeignKey(evento)
	@models.permalink
	def get_absolute_url(self):
		return ('observatorio.views.ver_vehiculo',(str(self.num_vehiculo),))

	def __unicode__(self):
		return unicode(self.num_vehiculo)

class rol_persona(models.Model):
	rol=models.CharField(max_length=45)

	def __unicode__(self):
		return self.rol

class gravedad_lesion(models.Model):
	gravedad=models.CharField(max_length=35)

	def __unicode__(self):
		return self.gravedad

class medidas_seguridad(models.Model):
	medida=models.CharField(max_length=45)

	def __unicode__(self):
		return self.medida

class muerte_escena(models.Model):
	descripcion=models.CharField(max_length=20)

	def __unicode__(self):
		return self.descripcion

class ocupacion(models.Model):
	ocupacion=models.CharField(max_length=50)

	def __unicode__(self):
		return self.ocupacion

class estado_civil(models.Model):
	estado_civil=models.CharField(max_length=15)

	def __unicode__(self):
		return self.estado_civil

class escolaridad(models.Model):
	escolaridad=models.CharField(max_length=20)

	def __unicode__(self):
		return self.escolaridad

class prioridad(models.Model):
	prioridad=models.CharField(max_length=15)

	def __unicode__(self):
		return self.prioridad

class persona(models.Model):
	sexo_choices=((0, 'Femenino'),(1, 'Masculino'))
	edad=models.IntegerField(null=True,blank=True)
	sexo=models.IntegerField(choices=sexo_choices,null=True, blank=True)
	rol=models.ForeignKey(rol_persona)
	gravedad_lesion=models.ForeignKey(gravedad_lesion)
	fecha_mort=models.DateTimeField(null=True, blank=True)
	num_amb=models.CharField(max_length=2, null=True,blank=True)
	operador=models.CharField(max_length=50, null=True,blank=True)
	prest_serv=models.CharField(max_length=50, null=True, blank=True)
	evento=models.ForeignKey(evento)
	vehiculo=models.ForeignKey(vehiculo, null=True,blank=True)
	clasificacion1=models.BooleanField(blank=True)
	clasificacion2=models.BooleanField(blank=True)
	medidas_seguridad=models.ForeignKey(medidas_seguridad)
	muerte_escena=models.ForeignKey(muerte_escena)
	ocupacion=models.ForeignKey(ocupacion)
	estado_civil=models.ForeignKey(estado_civil)
	escolaridad=models.ForeignKey(escolaridad)
	prioridad=models.ForeignKey(prioridad)

	def __unicode__(self):
		return unicode(self.id)

class tipo_licencia(models.Model):
	tipo=models.CharField(max_length=30)

	def __unicode__(self):
		return self.tipo

class conductor_alcoholizado(models.Model):
	alcoholizado=models.CharField(max_length=35)

	def __unicode__(self):
		return self.alcoholizado

class posicion_persona(models.Model):
	posicion=models.CharField(max_length=50)
	def __unicode__(self):
		return self.posicion

class tipo_accidente(models.Model):
	tipo=models.CharField(max_length=30)

	def __unicode__(self):
		return self.tipo

class interseccion_accidente(models.Model):
	interseccion=models.CharField(max_length=13)

	def __unicode__(self):
		return self.interseccion 

class escenario_impacto(models.Model):
	escenario=models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.escenario

class tipo_impacto(models.Model):
	tipo_impacto=models.CharField(max_length=50)

	def __unicode__(self):
		return self.tipo_impacto

class ubicacion_impacto(models.Model):
	ubicacion=models.CharField(max_length=20)

	def __unicode__(self):
		return self.ubicacion

class posicion_transeunte(models.Model):
	posicion=models.CharField(max_length=30)
	def __unicode__(self):
		return self.posicion

class direccion_inicial(models.Model):
	direccion=models.CharField(max_length=30)
	def __unicode__(self):
		return self.direccion

class conductor(models.Model):
	persona=models.OneToOneField(persona, primary_key=True)
	licencia=models.BooleanField()
	num_licencia=models.IntegerField()
	tipo_licencia=models.ForeignKey(tipo_licencia)
	conductor_alcoholizado=models.ForeignKey(conductor_alcoholizado)

	def __unicode__(self):
		return unicode(self.persona)
	
class pasajero(models.Model):
	persona=models.OneToOneField(persona, primary_key=True)
	posicion_persona=models.ForeignKey(posicion_persona)

	def __unicode__(self):
		return unicode(self.persona)


class transeunte(models.Model):
	persona=models.OneToOneField(persona, primary_key=True)
	marca_crucero_peatonal=models.BooleanField()
	banqueta=models.BooleanField()
	zona_escolar=models.BooleanField()
	tipo_impacto=models.ForeignKey(tipo_impacto)
	ubicacion_impacto=models.ForeignKey(ubicacion_impacto)
	posicion_transeunte=models.ForeignKey(posicion_transeunte)
	direccion_inicial=models.ForeignKey(direccion_inicial)
	interseccion_accidente=models.ForeignKey(interseccion_accidente)
	escenario_impacto=models.ForeignKey(escenario_impacto)
	tipo_accidente=models.ForeignKey(tipo_accidente)
	

	def __unicode__(self):
		return unicode(self.persona)
	
