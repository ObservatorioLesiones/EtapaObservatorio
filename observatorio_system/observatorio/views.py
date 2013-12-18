# Create your views here.
from django.template.response import TemplateResponse
from observatorio.models import evento

def home(request):
	return TemplateResponse(request,"home.html",{'eventos':evento.objects.all()})
