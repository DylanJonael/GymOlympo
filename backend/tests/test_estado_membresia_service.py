from datetime import datetime, timedelta
from types import SimpleNamespace

from backend.app.services.estado_membresia_service import build_membership_status_payload


def build_pago(days_offset: int, duration: int = 30, tipo: str = "Mensual"):
    fecha_pago = datetime.now() + timedelta(days=days_offset)
    return SimpleNamespace(
        Fecha_Pago=fecha_pago,
        membresia=SimpleNamespace(Duracion_Dias=duration, Tipo=tipo),
    )


def test_returns_sin_pagos_when_no_payment():
    payload = build_membership_status_payload(None)

    assert payload["estado"] == "SIN_PAGOS"
    assert payload["fecha_vencimiento"] is None


def test_returns_activa_when_membership_has_many_days_left():
    payload = build_membership_status_payload(build_pago(days_offset=-2, duration=30))

    assert payload["estado"] == "ACTIVA"
    assert payload["dias_restantes"] > 5


def test_returns_proxima_a_vencer_when_membership_is_close_to_expiration():
    payload = build_membership_status_payload(build_pago(days_offset=-27, duration=30))

    assert payload["estado"] == "PROXIMA_A_VENCER"


def test_returns_vencida_when_membership_expired():
    payload = build_membership_status_payload(build_pago(days_offset=-40, duration=30))

    assert payload["estado"] == "VENCIDA"
