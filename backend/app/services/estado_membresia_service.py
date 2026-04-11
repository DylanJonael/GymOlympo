from datetime import datetime, timedelta


WARNING_DAYS = 5


def build_membership_status_payload(last_pago):
    if last_pago is None:
        return {
            "estado": "SIN_PAGOS",
            "fecha_ultimo_pago": None,
            "fecha_vencimiento": None,
            "membresia": None,
            "dias_restantes": None,
        }

    fecha_pago = last_pago.Fecha_Pago
    duracion_dias = last_pago.membresia.Duracion_Dias if last_pago.membresia else 0
    fecha_vencimiento = fecha_pago + timedelta(days=duracion_dias)
    today = datetime.now()
    dias_restantes = (fecha_vencimiento.date() - today.date()).days

    if fecha_vencimiento < today:
        estado = "VENCIDA"
    elif dias_restantes <= WARNING_DAYS:
        estado = "PROXIMA_A_VENCER"
    else:
        estado = "ACTIVA"

    return {
        "estado": estado,
        "fecha_ultimo_pago": fecha_pago,
        "fecha_vencimiento": fecha_vencimiento,
        "membresia": last_pago.membresia.Tipo if last_pago.membresia else None,
        "dias_restantes": dias_restantes,
    }
