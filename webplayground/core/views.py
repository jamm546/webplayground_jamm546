# from django.shortcuts import render

# def home(request):
#     return render(request, "core/home.html")

# def sample(request):
#     return render(request, "core/sample.html")

#DEBEMOS ADACTAR A VISTAS ORIENTADAS A CLASES, ELLAS ESTAN EN VISTAS ORIENTAS A FUNCIONES
#https://docs.djangoproject.com/en/2.0/ref/class-based-views/base/#django.views.generic.base.TemplateView
#Tenemos que hacer los cambios en urls.py para adaptarlo a las clases
from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name = "core/home.html"
    #ES MUY TEDIOSO HACER TODO ESTOY POR ELLO PODEMOS HACER LO SIGUIENTE
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     #context['latest_articles'] = Article.objects.all()[:5]
    #     context['title'] = 'My Super Web PlayGround' #diccionario de conexto, si voy al home.html podemos mosrarla
    #     return context
    #END / ES MUY TEDIOSO HACER TODO ESTOY POR ELLO PODEMOS HACER LO SIGUIENTE
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title':'My Super Web PlayGround'})

class SamplePageView(TemplateView):
    template_name = "core/sample.html"