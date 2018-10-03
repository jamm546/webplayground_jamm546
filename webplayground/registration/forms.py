#lo creamos nosotros
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres como maximo y debe ser valido.")

    class Meta:
        model = User
        fields = {"username", "email", "password1", "password2"}
        #funciona email porque ya existe solo es decirle que lo use
        #si este campo no existiera es imposible hacerlo de esta manera
        #Luego nos vamos a views.py y lo importamos
        #si ponermos un widget aca estariamos danando todas las validaciones
    
    #Vamos a validar que email sea unico, porque por defecto este era opcional
    #si cambiamos el clean ya no funcionaria, tiene que tener relacion con el campo del modelo
    def clean_email(self):
        email = self.cleaned_data.get("email") # este es el del formulario
        if User.objects.filter(email=email).exists(): #busca en la base de dato por el filtro que pusimos
            raise forms.ValidationError("El email ya esta registrado, pruena con otro.")
        return email

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link']
        widget ={
            'avatar': forms.ClearableFileInput(attrs={'class':'form-control-file mb-3'}),
            'bio': forms.Textarea(attrs={'class':'form-control mb-3', 'rows':3, 'placeholder':'Biografia'}),
            'link': forms.URLInput(attrs={'class':'form-control mb-3', 'placeholder':'Enlace'})
        }

class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres como maximo y debe ser valido.")
    class Meta:
        model = User
        fields = ['email']
        #no ponemos los widgets aca porque django tiene sus validaciones, lo creamos en tiempo de ejecucion y seria en la propia vista
    def clean_email(self):
        email = self.cleaned_data.get("email") # este es el del formulario
        #contiene si lo han modificado, solo dejamos guardar el email si no lo ha tenido un usuario antes
        if 'email' in self.changed_data:     
            if User.objects.filter(email=email).exists(): #busca en la base de dato por el filtro que pusimos
                raise forms.ValidationError("El email ya esta registrado, pruena con otro.")
        return email