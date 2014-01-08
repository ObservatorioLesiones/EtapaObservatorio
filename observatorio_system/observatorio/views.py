# Create your views here.
from django.db.models import Q
from django.template.response import TemplateResponse
from observatorio.models import evento
from observatorio.models import Delegacion

def home(request):
	return TemplateResponse(request,"home.html",{'eventos':evento.objects.all()})

def ver_evento(request, num_evento):
	return TemplateResponse(request,"evento.html",{'evento':evento.objects.get(num_evento=num_evento)})

def delegacion_c(request):
	query = request.GET.get('q', '')
	item  = Delegacion.objects.all()
	if query:
		qset = (Q(delegacion__nombre_d__icontains=query))
		results = evento.objects.filter(qset).distinct()
	else:
		results=[]
	return TemplateResponse(request,"delegacion_c.html", {"results":results,"query":query, 'item':item })
