import time
import requests
import smtplib
from bs4 import BeautifulSoup

URL = 'https://www.amazon.ca/gp/product/B00BMEI9RO/ref=ppx_yo_dt_b_asin_title_o03_s00?ie=UTF8&psc=1'


def check_price():
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/79.0.3945.130 Safari/537.36'}
    page = requests.get(URL, headers = headers)
    soup = BeautifulSoup(page.content, 'lxml')
    price_string = soup.find(id="priceblock_ourprice").get_text()
    price_float = float(str(price_string).replace('CDN$', ''))

    if(price_float < 12):
        send_mail()
    print(price_float)


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('modidhaval1121991@gmail.com', 'oxhcxvzjxjevnjow')

    subject = 'Price Fell Down !!!'
    body = 'Check this link ', URL
    msg = f"Subject: {subject}\n\n {body} "

    server.sendmail(
        'modidhaval1121991@gmail.com',
        'dhavalmodi556@gmail.com',
        msg
    )

    print('Email has been sent !!!')

    server.quit()


while():
    check_price()
    time.sleep(60 * 60 * 24)
