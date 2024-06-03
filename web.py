import bs4
import requests

from kripto_valuta import KriptoValuta


def dohvati_5_kripto_valuta() -> list[KriptoValuta]:
    URL = "https://coinmarketcap.com/"
    response = requests.get(URL)
    soup = bs4.BeautifulSoup(response.content, "html.parser")

    svi_html_kripto_retci = soup.find_all("tr")

    kripto_valute = []
    
    for redak in svi_html_kripto_retci[1:6]:
        stupci = redak.find_all("td")
        kripto_valuta = parsiraj_jedan_html_redak(stupci)
        kripto_valute.append(kripto_valuta)

    return kripto_valute


def parsiraj_jedan_html_redak(stupci: bs4.ResultSet) -> KriptoValuta:
    # dohvati željene podatke
    ime = stupci[2].find("p").text
    vrijednost = stupci[3].get_text()
    trend_24h_postotak = stupci[5].get_text()
    trend_24h_html_class = stupci[5].find_all("span")[-1]["class"]  # icon-Caret-up/icon-Caret-down
    trend_7d_postotak = stupci[6].get_text()
    trend_7d_html_class = stupci[6].find_all("span")[-1]["class"]  # icon-Caret-up/icon-Caret-down

    # parsiraj 24h trend
    if "icon-Caret-up" in trend_24h_html_class:
        trend_24h = "up"
    elif "icon-Caret-down" in trend_24h_html_class:
        trend_24h = "down"
    else:
        trend_24h = "Unknown"

    # parsiraj 7d trend
    if "icon-Caret-up" in trend_7d_html_class:
        trend_7d = "up"
    elif "icon-Caret-down" in trend_7d_html_class:
        trend_7d = "down"
    else:
        trend_7d = "Unknown"

    # vrati KriptoValutu
    return KriptoValuta(
        ime=ime,
        vrijednost=vrijednost,
        trend_24h=trend_24h,
        trend_24h_postotak=trend_24h_postotak,
        trend_7d=trend_7d,
        trend_7d_postotak=trend_7d_postotak
    )
