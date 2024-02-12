from django import forms

class Form_Musico(forms.Form):
    nombre = forms.CharField(max_length = 30)
    instrumento = forms.CharField(max_length = 30)
    banda = forms.CharField(max_length = 30)

class Form_Album(forms.Form):
    nombre_disco = forms.CharField(max_length = 30)
    banda = forms.CharField(max_length = 30)
    lanzamiento = forms.IntegerField()
    genero = forms.CharField(max_length = 30)

class Form_Banda(forms.Form):
    nombre = forms.CharField(max_length=100)
    integrantes = forms.IntegerField()