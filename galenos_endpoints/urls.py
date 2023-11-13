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
