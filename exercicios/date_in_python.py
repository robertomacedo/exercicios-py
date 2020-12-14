import requests
from datetime import datetime

def hora(timezone):
    url = 'http://worldtimeapi.org/apr/timezone' + timezone

    resp = requests.get(url)

    hora = datetime.fromisoformat(resp.json()['datetime'])

    return hora
def timezones_disponivel():
    url = 'http://worldtimezone.org/api/timezone'
    resp = requests.get(url)
    return resp.json()


