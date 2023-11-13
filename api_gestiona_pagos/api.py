# Westeros/stark/api.py
from django.shortcuts import get_object_or_404
from ninja import Router
from api_gestiona_pagos.schemas import PagoIn, PagoOut
from api_gestiona_pagos.models import Pago

router = Router()


@router.post("/crea", response=PagoOut, url_name="create_pago")
def create_pago(request, payload: PagoIn):
    pago = Pago.objects.create(**payload.dict())
    return pago


@router.get("/lista", response=list[PagoOut], url_name="list_pagos")
def list_pagos(request):
    return Pago.objects.all()


@router.get("/lista/{int:pago_id}", response=PagoOut, url_name="pago")
def get_pago(request, pago_id):
    return get_object_or_404(Pago, id=pago_id)


@router.put("/modifica/{int:pago_id}", response=PagoOut)
def update_pago(request, pago_id, payload: PagoIn):
    pago = get_object_or_404(Pago, id=pago_id)

    for name, value in payload.dict().items():
        setattr(pago, name, value)

    pago.save()
    return pago


@router.delete("/elimina/{int:pago_id}")
def update_pago(request, pago_id):
    pago = get_object_or_404(Pago, id=pago_id)
    pago.delete()

    return {"success": True}
