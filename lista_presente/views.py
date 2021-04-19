from django.shortcuts import render
from lista_presente.models import ListaPresentes
# Create your views here.
def lista_presentes(request):
    items = ListaPresentes.objects.all()
    context = {"items": items}
    return render(request,"lista_presente/lista_presentes.html",context)