from typing import NamedTuple


class Cotizacion (NamedTuple):
    moneda: str
    compra: float
    venta:  float