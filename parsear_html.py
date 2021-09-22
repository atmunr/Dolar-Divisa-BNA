from bs4 import BeautifulSoup
from cotizacion import Cotizacion


def fecha_de_tbody_tr (tr):
    return tr.find_all('td')[-1].string


def tbody_tr_con_fecha_dada (html, fecha):
    soup = BeautifulSoup(html, 'html.parser')
    return [
        tr for tr in soup.find_all('tr')
        if tr.parent.name == 'tbody' and
           fecha_de_tbody_tr(tr) == fecha
    ]


def parsear_cotizacion_dolar (tbody_tr_list):
    try:
        return Cotizacion(
            moneda = 'Dolar',
            compra = float(tbody_tr_list[0].find_all('td')[1].string),
            venta  = float(tbody_tr_list[0].find_all('td')[2].string)
        )
    except IndexError:
        return None


def parsear_cotizacion_euro (tbody_tr_list):
    try:
        return Cotizacion(
            moneda = 'Euro',
            compra = float(tbody_tr_list[1].find_all('td')[1].string),
            venta  = float(tbody_tr_list[1].find_all('td')[2].string)
        )
    except IndexError:
        return None


def parsear_cotizaciones_con_fecha_dada (html, fecha):
    trs = tbody_tr_con_fecha_dada(html, fecha)
    return parsear_cotizacion_dolar(trs), parsear_cotizacion_euro(trs)