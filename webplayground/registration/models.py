from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

#en el caso que otro usuario quiere registrar una imagen con un mismo numero
#se le crea una clave a la imagen de esta maneja no se reemplaza la que ya existe
def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename
# Create your models here.
#para los perfiles privados lo vamos a manejar desde registrations
class Profile(models.Model):
    #vamos a crear una relacion uno a uno con user, por ello lo importamos tambien
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #begin lo vamos a cambiar para que en el avatar siempre este la ultima imagen, y no gastar espacio dejando
    #imagenes viejas, es espacio es valioso y cuesta dinero
    #avatar = models.ImageField(upload_to='profiles', null=True, blank=True)
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    #end
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ['user__username']
    #recordar que si vamos a trabar con imagenes debemos tener instalado Pilow en el entorno virtual
    #   y configurarlo en settings.py, al final del fichero

    # EN DJANGO TENEMOS TRES TIPO DE RELACION
    # OneToOneField (1:1) 1 usuario - 1 perfil
    # ForeignKeyField (1:N) 1 autor <- N entradas
    # ManyToManyField (N: M) N entradas <-> M categorias

#vamos a crear una senal, esto para evitar que un0 usuario se registre y se quede sin perfil, 
#lo cual nos puede generar errores en nuestro porta
#usaremos un decorador, para ejecutar el evento despues de guardar el usuario
#consultar la documentacion de esta clase seccion 4 clase 78
@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False): # con este aseguramos que se ejecute solo la primera vez
        Profile.objects.get_or_create(user=instance)
        #print("Se acaba de crear un usuario y su perfil enlazado")
        #python manage.py shell, para ir y verificar si es verdad que se creo el perfil
        #>>> from registration.models import Profile
        #>>> Profile.objects.get(user__username='test8')
        #retorna una instancion por ello asumimos que existe >><Profile: Profile object (2)>