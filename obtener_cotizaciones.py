import requests
import datetime
from parsear_html import parsear_cotizaciones_con_fecha_dada


def solicitar_html_con_cotizaciones_de_divisas_de_api (fecha):
    try:
        res = requests.get(
            url    = 'http://bna.com.ar/Cotizador/HistoricoPrincipales',
            params = {
                'id'         : 'monedas',
                'fecha'      : fecha,
                'filtroEuro' : 1,
                'filtroDolar': 1
            }
        )
    except: return "" # fibertel lcdtm T_T
    return res.text


def obtener_cotizaciones_de_divisas (fecha):
    fecha_string = fecha.strftime("%-d/%-m/%Y")
    html = solicitar_html_con_cotizaciones_de_divisas_de_api(fecha_string)
    return parsear_cotizaciones_con_fecha_dada(html, fecha_string)