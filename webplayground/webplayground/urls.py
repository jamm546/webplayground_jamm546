"""webplayground URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pages.urls import pages_patterns
#CONFIGURANDO LOS ARCHIVOS MEDIA
from django.conf import settings
#END / CONFIGURANDO LOS ARCHIVOS MEDIA
from profiles.urls import profiles_patterns
from messenger.urls import messenger_patterns

urlpatterns = [
    path('', include('core.urls')),
    #path('pages/', include('pages.urls')), #hace referencia al path pages
    path('pages/', include(pages_patterns)),
    path('admin/', admin.site.urls),
    #Paths de Auth (Lo agregamos nosoros clase 66), para acceder a ellas 127.0.0.1:8000/accounts
    path('accounts/', include('django.contrib.auth.urls')),
    #Paths de Registrations (Lo agregamos nosoros clase 66), para acceder a ellas 127.0.0.1:8000/accounts
    path('accounts/', include('registration.urls')), #aumentamos la lista de path dejando accounts/
    path('profiles/', include(profiles_patterns)),
    path('messenger/', include(messenger_patterns)),
]

#CONFIGURANDO LOS ARCHIVOS MEDIA'
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#END / CONFIGURANDO LOS ARCHIVOS MEDIA