from datetime import date, timedelta
from obtener_cotizaciones import obtener_cotizaciones_de_divisas


d1 = date(day =  1, month = 9, year = 2021)
d2 = date(day = 22, month = 9, year = 2021)


while d1 < d2:
    dolar, euro = obtener_cotizaciones_de_divisas(d1)
    if not dolar is None: # por ejemplo en los findes no hay cotizaciones
        print(
            d1.strftime("%d/%m/%Y|  "),
            'Compra dolar divisa:', '{:f}'.format(dolar.compra), '  '
             'Venta dolar divisa:', '{:f}'.format(dolar.venta),
            end = '\n\n'
        )
    d1 += timedelta(days = 1) 