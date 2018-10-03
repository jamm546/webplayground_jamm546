#from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required # unico que tiene
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import Page
#nos importamos el formulario 
from .forms import PageForm

class StaffRequiredMixin(object): # BUSCAR DOCUMENTACION DE MIXIN, EN LA CLASE SECCION 4 CLASE 64 ESTA EL ENLACE
    """
    Este Mixin requerira que el usuario sea miembro del staff
    Estamos reimplementetando el metodo dispatch
    """
    #esta funcion por ser de django no podemos decorar como sabemos, tiene sus pasos, por ello dos libreriras
    #con este decorador nos da la particularidad de que si requiere validacion apenas valida te regresa donde estabas, le pone un next
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        #NOS PODEMOS AHORRAR ESTAS LINEAS USANDO DECORADORES, PARA ELLO IMPORTAMOS DOS LIBRERIAS
        #from django.contrib.admin.views.decorators import staff_member_required
        #from django.utils.decorators import method_decorator
        #if not request.user.is_staff:
        #    return redirect(reverse_lazy('admin:login')) #tenemos que importar rediret en la cabecera
        #END / NOS PODEMOS AHORRAR ESTAS LINEAS USANDO DECORADORES, PARA ELLO IMPORTAMOS DOS LIBRERIAS
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)


# Create your views here.
# def pages(request):
#     pages = get_list_or_404(Page)
#     return render(request, 'pages/pages.html', {'pages':pages})

# def page(request, page_id, page_slug):
#     page = get_object_or_404(Page, id=page_id)
#     return render(request, 'pages/page.html', {'page':page})

#ADAPTAMOS TODO A CLASES
#https://docs.djangoproject.com/en/2.0/ref/class-based-views/generic-display/#django.views.generic.list.ListView
class PageListView(ListView):
    model = Page # ahora nos vamos a urls.py de pages

#AHORA VAMOS A LA DEL DETALLE
#https://docs.djangoproject.com/en/2.0/ref/class-based-views/generic-display/#django.views.generic.detail.DetailView
class PageDetailView(DetailView):
    model = Page # ahora nos vamos a urls.py de pages

#https://docs.djangoproject.com/en/2.0/ref/class-based-views/generic-editing/#django.views.generic.edit.CreateView
#class PageCreate(CreateView):
#class PageCreate(StaffRequiredMixin, CreateView): #lo agregamos con prioridad, mas a la izquierda el MIXIN
@method_decorator(staff_member_required, name='dispatch') #le indicamos el metodo con name
class PageCreate(CreateView): #con el decorador ahora no hace falta el MIXIN, se coloca asi
    model = Page # le pasamos el modelo
    form_class = PageForm #vamos otra vez al forms.py para agregar los estilos
    #Como PageForm tiene fields, podemos comentar la liena de abajo
    #fields = ['title', 'content', 'order'] # los campos que queremos que pueda editar
    #luego nos vamos a urls.py y agregamos un nuevo path
    #PAra que no de error al momento de guardar importarmos reverse y ponemos el siguiente codigo
    #sin embargo hacer todo esto es muy tedioso, por ello se cambio a
    # def get_success_url(self):
    #     return reverse('pages:pages')
    #END /sin embargo hacer todo esto es muy tedioso, por ello se cambio a
    # IMPORTAMOS reverse_lazy, y hacemos lo siguiente
    success_url = reverse_lazy('pages:pages')

    #VALIDAMOS QUE SI EL USUARIO NO ESTA EN SESSION NO PUEDA ENTRAR SI NO QUE LO MANDE A VALIDAR SESSION
    #SIN ESTE CODIGO PUEDEN HACER CAMBIOS SIN VALIDAR SESION
    #Existen los Mixin para no tener que escribir todo este codigo en cada una de las vistas
        #la vamos a crear arriba del todo
    # def dispatch(self, request, *args, **kwargs):
    #     if not request.user.is_staff:
    #         return redirect(reverse_lazy('admin:login')) #tenemos que importar rediret en la cabecera
    #     return super(PageCreate, self).dispatch(request, *args, **kwargs)
    #END / #Existen los Mixin para no tener que escribir todo este codigo en cada una de las vistas

#https://docs.djangoproject.com/en/2.0/ref/class-based-views/generic-editing/#django.views.generic.edit.UpdateView
#class PageUpdate(UpdateView):
#class PageUpdate(StaffRequiredMixin, UpdateView): #LE AGREGAMOS TAMBIEN EL MIXIN
@method_decorator(staff_member_required, name='dispatch')
class PageUpdate(UpdateView): #LE AGREGAMOS TAMBIEN EL MIXIN
    model = Page
    form_class = PageForm #vamos otra vez al forms.py para agregar los estilos
    #fields = ['title', 'content', 'order']
    #para usar otro formulario le pasamos este sufijo por defecto, duplicamos el formulario create y lo modificamos
    #luego vamos al fichero urls y creamos una nueva entrada o path
    template_name_suffix = '_update_form' 
    #luego definimos el sussecs url, si lo ponemos como el create nos manda a la lista de page
    #pero en este caso queremos que se quete en la pagina update para ver los cambios
    ######success_url = reverse_lazy('pages:pages') 
    #Lo hacemos de la siguiente manera
    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'
        #ahora tenemos que ir a urls y volver a modificar el path
        #pero como refresca tan rapido el usuario no sabe si se actualizo, por ello vamos a infromarle
        # le concatenamos un ok, luego hacemos los cambios en el page_update_form.html para mostrar el mensaje
        #tambien tenemos que ir page_detail.html para poner el enlace en el boton editar
        #tambien lo mismo en el page_list.html

#https://docs.djangoproject.com/en/2.0/ref/class-based-views/generic-editing/#django.views.generic.edit.DeleteView
#class PageDelete(DeleteView):
#class PageDelete(StaffRequiredMixin, DeleteView): #LE AGREGAMOS TAMBIEN EL MIXIN
@method_decorator(staff_member_required, name='dispatch')    
class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')
    #ahora vamos a crear la url
    #por ultimo vamos a page_list.html y agregamos el urls para eliminar
    #dentreo del  .html confirm_delete se refiere al object pero tambien funciona colocando page