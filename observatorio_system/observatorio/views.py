# Create your views here.
from django.db.models import Q
from django.template.response import TemplateResponse
from observatorio.models import evento
from observatorio.models import Delegacion
from observatorio.models import Ciudad
from observatorio.models import Municipio
from observatorio.models import Descripcion_Vial
from observatorio.models import vehiculo
from observatorio.models import persona


def home(request):
    return TemplateResponse(request, "home.html", {'eventos': evento.objects.all()})

def eventos(request):
    return TemplateResponse(request, "eventos.html", {'eventos': evento.objects.all()})

def ver_evento(request, num_evento):
    eventos=evento.objects.get(id=num_evento)
    personas = eventos.persona_set.filter()
    vehiculos=eventos.vehiculo_set.filter()
    return TemplateResponse(request, "evento.html", {"evento":eventos,"personas":personas, "vehiculos":vehiculos})


def delegacion_c(request):
    query = request.GET.get('q', '')
    item = Delegacion.objects.all()
    if query:
        qset = (Q(delegacion__nombre_delegacion__icontains=query))
        results = evento.objects.filter(qset).distinct()
    else:
        results = []
    return TemplateResponse(request, "delegacion_c.html", {"results": results, "query": query, 'item': item})


def ciudad_c(request):
    query = request.GET.get('q', '')
    item = Ciudad.objects.all()
    if query:
        qset = (Q(ciudad__nombre_ciudad__icontains=query))
        results = evento.objects.filter(qset).distinct()
    else:
        results = []
    return TemplateResponse(request, "ciudad_c.html", {"results": results, "query": query, 'item': item})


def municipio_c(request):
    query = request.GET.get('q', '')
    item = Municipio.objects.all()
    if query:
        qset = (Q(municipio__nombre_municipio__icontains=query))
        results = evento.objects.filter(qset).distinct()
    else:
        results = []
    return TemplateResponse(request, "municipio_c.html", {"results": results, "query": query, 'item': item})


def descvial_c(request):
    query = request.GET.get('q', '')
    item = Descripcion_Vial.objects.all()
    if query:
        qset = (Q(descripcion_vial__descripcion__icontains=query))
        results = evento.objects.filter(qset).distinct()
    else:
        results = []
    return TemplateResponse(request, "descvial_c.html", {"results": results, "query": query, 'item': item})


def vehiculos_c(request):
    return TemplateResponse(request, "vehiculos_c.html", {'item': vehiculo.objects.all()})


def ver_vehiculo(request, num_vehiculo):
    item = vehiculo.objects.get(id=num_vehiculo)
    query = item.persona_set.filter()
    return TemplateResponse(request, "vehiculo.html", {'item': item, "query":query})

def personas_c(request):
    return TemplateResponse(request, "personas_c.html", {'item': persona.objects.all()})

def ver_persona(request, num_persona):
    item = persona.objects.get(id=num_persona)
    return TemplateResponse(request, "persona.html", {'item': item})





