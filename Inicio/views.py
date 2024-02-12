from django.shortcuts import render, HttpResponse
from Inicio import models, forms
from django.http import HttpResponse


def inicio(request):
    return render(request,'base.html')

def bandas(request):
      if request.method == "POST":
            miFormulario = forms.Form_Banda(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  banda = models.Banda(nombre=informacion["nombre"], integrantes=informacion["integrantes"])
                  banda.save()
                  return render(request, "bandas.html")
      else:
            miFormulario = forms.Form_Banda()
      return render(request, "bandas.html", {"miFormulario": miFormulario})


def musicos(request):
      if request.method == "POST":
            miFormulario = forms.Form_Musico(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  musico = models.Musico(nombre=informacion["nombre"], instrumento=informacion["instrumento"], banda=informacion["banda"])
                  musico.save()
                  return render(request, "musicos.html")
      else:
            miFormulario = forms.Form_Musico()
      return render(request, "musicos.html", {"miFormulario": miFormulario})

def discos(request):
      if request.method == "POST":
            miFormulario = forms.Form_Album(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  album = models.Album(nombre_disco=informacion["nombre_disco"], banda=informacion["banda"], lanzamiento=informacion["lanzamiento"], genero=informacion["genero"])
                  album.save()
                  return render(request, "discos.html")
      else:
            miFormulario = forms.Form_Album()
      return render(request, "discos.html", {"miFormulario": miFormulario})

"""def buscar(request):
      if request.GET['nombre']:
            nombre = request.GET['nombre']
            bandas = models.Banda.objects.filter(nombre__icontains=nombre)
            return render(request, 'busqueda.html', {'nombre': nombre, 'bandas': bandas})
      else:
            respuesta = 'No enviaste datos.'
            return HttpResponse(respuesta)"""


def buscar(request):
    if request.method == 'GET':
        anio = request.GET.get('anio_lanzamiento')
        discos = models.Album.objects.filter(lanzamiento=anio)
        return render(request, 'busqueda.html', {'discos': discos})
    else:
        return render(request, 'busqueda.html')
