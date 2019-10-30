from bs4 import BeautifulSoup
import requests
import sys


def buscar_significado(texto):
    url = "https://dle.rae.es/?id=KYtLWBc"

    r = requests.get(url)
    if r.status_code != 200:
        sys.stderr.write("! Error {} retrieving url {}".format(r.status_code, url))
        return None

    return r.text