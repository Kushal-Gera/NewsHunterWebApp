import json
import requests
from bs4 import BeautifulSoup
from firebase import firebase
import smtplib


def check_price(url, target_price):

    USER_AGENTS = [('Mozilla/5.0 (X11; Linux x86_64) '
                     'AppleWebKit/537.36 (KHTML, like Gecko) '
                     'Chrome/57.0.2987.110 '
                     'Safari/537.36'),  # chrome
                    ('Mozilla/5.0 (X11; Linux x86_64) '
                     'AppleWebKit/537.36 (KHTML, like Gecko) '
                     'Chrome/61.0.3163.79 '
                     'Safari/537.36'),  # chrome
                    ('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) '
                     'Gecko/20100101 '
                     'Firefox/55.0'),  # firefox
                    ('Mozilla/5.0 (X11; Linux x86_64) '
                     'AppleWebKit/537.36 (KHTML, like Gecko) '
                     'Chrome/61.0.3163.91 '
                     'Safari/537.36'),  # chrome
                    ('Mozilla/5.0 (X11; Linux x86_64) '
                     'AppleWebKit/537.36 (KHTML, like Gecko) '
                     'Chrome/62.0.3202.89 '
                     'Safari/537.36'),  # chrome
                    ('Mozilla/5.0 (X11; Linux x86_64) '
                     'AppleWebKit/537.36 (KHTML, like Gecko) '
                     'Chrome/63.0.3239.108 '
                     'Safari/537.36'),
                    ('Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'), ]

    for u in USER_AGENTS:
        HEADERS = {"User-Agent" : u}
        data = requests.get(url, headers=HEADERS).text
        soup = BeautifulSoup(data, "html.parser")

        price_item = soup.find(id="priceblock_ourprice")
        if price_item:
            price = price_item.get_text().strip()[1:].strip()
            return price <= target_price
            break;

    return 0


def send_email(data_dict):
    SENDER_EMAIL = "tvmi1891@gmail.com"
    PASSWORD = "8888inder"
    SERVER = smtplib.SMTP('smtp.gmail.com', 587)

    SERVER.ehlo()
    SERVER.starttls()
    SERVER.login(SENDER_EMAIL, PASSWORD)

    print("sending email....")

    # message = "Subject:{Subject}" + "/n/n" + {body}
    message = "Subject:"+data_dict["product_name"]+" price has fell down !!" + "\n\n" + "Price for \""+data_dict["product_name"]+"\" has reached below your target price of \"" + data_dict["target_price"] + "\"!! \n\nClick the link below to buy now," + "\n\n" + data_dict["product_url"]

    SERVER.sendmail(SENDER_EMAIL, data_dict["your_email"], message)
    SERVER.quit()


####################################  RUNABLE CODE HERE ::  ######################################
fb = firebase.FirebaseApplication("https://barcode-scanner-92b37.firebaseio.com/", None)
data = fb.get("/Products", "")


for d in data:
    if check_price(data[d]["product_url"], data[d]["target_price"]):
        print("Cheaper Available")
        send_email(data[d])
        fb.delete("/Products", d)
    else:
        print("Costly !!")



####################################
