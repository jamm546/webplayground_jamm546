from django.test import TestCase
#nosotros cargamos los modelos que queremos usar
from .models import Profile
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('prueba', 'prueba@ejemplo.com', 'prueba1234')
    
    #puede ser cualquier nombre pero que inicie con test_
    def test_profile_exists(self):
        exists = Profile.objects.filter(user__username='prueba').exists()
        self.assertEqual(exists, True)

    #para ejecutarlo lo hacemos por la consola con el comando
    #python manage.py test registration
    #seccion 4 clase 79, documentacion sobre estos test de prueba