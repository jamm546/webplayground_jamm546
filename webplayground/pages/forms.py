#ESTE ARCHIVO LO CREAMOS
from django import forms
from .models import Page

class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ['title', 'content', 'order'] # los campos que queremos que edite
        #ahora vamos al fichero views.py para realizar los cambios
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Titulo'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}), #ckeditor no creo que funcione placeholder
            'order': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Orden'}),
        }
        #content no esta cargando bien el ckeditor, buscamo en la web del componente para ver
        #cuales son los archivos estaticos que debemos cargar
        #y pegamos en el codigo pages_menu.html, porque en esta
        #porque el menu se carga en todas las demas
        #https://github.com/django-ckeditor/django-ckeditor
        labels = {
            'title': '', #si lo ponemos vacios queremos decir que no muestre nada
            'content': '',
            'order': '',
        }