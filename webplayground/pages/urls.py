from django.urls import path
#from . import views
from .views import PageListView, PageDetailView, PageCreate, PageUpdate, PageDelete

# urlpatterns = [
#     path('', PageListView.as_view(), name='pages'),
#     path('<int:pk>/<slug:slug>/', PageDetailView.as_view(), name='page'),
#     path('create/', PageCreate.as_view(), name='create'),
# ]
#le vamos a poner un nombre cualquiera
pages_patterns = ([
    path('', PageListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', PageDetailView.as_view(), name='page'),
    path('create/', PageCreate.as_view(), name='create'),
    path('update/<int:pk>/', PageUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', PageDelete.as_view(), name='delete'),
], 'pages')
#ahora nos da error en el urls.py global, vamos a el y hacemos unos cambios
#y vamos a importarnos-> from pages.urls import pages_patterns
#tambien tenemos que ir a los templates y hacer unos cambios en el base.html {% url 'pages:pages' %}
#luego tambien tenemos que cambiarlo en el pages_menu.html {% url 'pages:pages' %}
#Y tambien se habia generado un urls en el page_list.html {% url 'pages:page' page.id page.title|slugify %}