# Westeros/stark/schemas.py
from ninja import ModelSchema
from api_gestiona_pagos.models import Pago


class PagoIn(ModelSchema):
    class Config:
        model = Pago
        model_exclude = [
            "id",
            "fecha_pago",
        ]


class PagoOut(ModelSchema):
    class Config:
        model = Pago
        model_fields = "__all__"
