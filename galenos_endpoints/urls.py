from django.contrib import admin
from django.urls import path

from ninja import NinjaAPI

from api_gestiona_pagos.api import router as pago_router
from django.views.generic import RedirectView

administracion = NinjaAPI()
administracion.add_router("/gestion-pagos/", pago_router)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("administracion/", administracion.urls),
    path("", RedirectView.as_view(url="/administracion/docs"), name="redirect-to-docs"),
]
https://github.com/docker/compose/releases/download/v2.23.0/
sudo curl -L https://github.com/docker/compose/releases/download/v2.23.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose