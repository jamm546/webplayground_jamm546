#from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreationFormWithEmail, ProfileForm, EmailForm
from django.views.generic import CreateView
#por ProfileUpdate
#from django.views.generic.base import TemplateView
#para verificar que el usuario este autenticado y poder modificar su perfil
#OTRA CLASE SE CAMBIO A
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django import forms
from .models import Profile

# Create your views here.
class SignUpView(CreateView):
    #form_class = UserCreationForm    
    form_class = UserCreationFormWithEmail    
    template_name = 'registration/signup.html'
    def get_success_url(self):
         return reverse_lazy('login')+'?register'
    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()
        #Modificar en tiempo real, con F12 buscamos lo nombres de los input
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombre de Usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Direccion email'}) #se agrego cuando se incluyo el email
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Contrasena'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Repite la contrasena'})
        #repetir otra vez los tres, es mejor ir al signup.html y ocultar los laberl
        #y ponemos un style con label{display:none}
        #form.fields['username'].label = ''
        #form.fields['password'].label = ''
        #form.fields['password2'].label = ''
        return form
    
#solo es accesible si el usuario esta autenticado
#importamos los decoradores configurado para validar esto
@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    #model = Profile
    form_class = ProfileForm
    #fields = ['avatar', 'bio', 'link']
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    #las UpdateView tienen un metodo, con esto evitamos que el usuario vea su ID
    def get_object(self):
        #recuerperar el object que se va a editar
        #Como no existe el get nos da error, para ello vamos a usar otro metodo
        #return Profile.objects.get(user=self.request.user)
        #si no lo encuentra lo crea,asi que no podemos ponerlo directo en el return, porque devuelve una tupla
        profile, create = Profile.objects.get_or_create(user=self.request.user)
        return profile

@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
    #model = Profile
    form_class = EmailForm
    #fields = ['avatar', 'bio', 'link']
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_email_form.html'

    #las UpdateView tienen un metodo, con esto evitamos que el usuario vea su ID
    def get_object(self):
        return self.request.user

    def get_form(self, form_class=None):
        form = super(EmailUpdate, self).get_form()
        #Modificar en tiempo real, con F12 buscamos lo nombres de los input
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Email'})
        return form
        #luego nos vamos a las urls.py