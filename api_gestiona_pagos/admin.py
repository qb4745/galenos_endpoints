from django.contrib import admin

from .models import Pago


@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ("id", "medico_id", "monto", "tipo_pago", "fecha_pago")
    search_fields = ["medico_id", "tipo_pago"]
    list_filter = ["tipo_pago", "fecha_pago"]
