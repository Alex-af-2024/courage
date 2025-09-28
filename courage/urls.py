"""
URL configuration for courage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from rest_framework import routers # crea rutas de forma automática para la API
from actor.views import ActorViewSet # added-> class que indica como se manejan los actores en la API

router = routers.DefaultRouter() # Crear un router
router.register(r'actor', ActorViewSet) # Registrar el ViewSet con el router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)), # Incluye las URLs del router
]

"""#Con esto se crean las  rutas como:
/api/actor/ para listar y crear actores,
/api/actor/<id>/  para actualizar y eliminar actores."""