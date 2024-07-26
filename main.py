import requests
from bs4 import BeautifulSoup
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

email = "YOUR_EMAIL"
email_pass = "YOUR_EMIL_APP_PASSWORD"
to_email = "RECIPIENT_MAIL"


link = "https://www.flipkart.com/noise-icon-3-plus-2-hd-display-metal-dial-functional-crown-smartwatch/p/itm0e2e593fc38da?pid=SMWGUSWMBHV8DHWM&lid=LSTSMWGUSWMBHV8DHWMJZCR5B&marketplace=FLIPKART&store=ajy%2Fbuh&srno=b_1_1&otracker=browse&fm=organic&iid=en_2TvyZNiBuT1ab2G7m1-t6cp4dXZnlyHKCicqfQ-wnnAUeT2aOh4NzNr_DzvXXSEsbp9XXhCy7mTEZmG9AE3jNA%3D%3D&ppt=browse&ppn=browse&ssid=hgqvw1d3e80000001721990438863"
tag_name = 'div'
aclass = {"class":'Nx9bqj CxhGGd'}

target_amount = 1800
daily_checker_time = "04:13"

now_time_date = datetime.now().strftime("%d-%b-%Y %I:%M")
now_time = datetime.now().strftime("%I:%M")
now_date = datetime.now().strftime("%d-%b-%Y")

daily_price = []
price_dates = []




def price(tag_name, aclass):
    r = requests.get(link)
    soup = BeautifulSoup(r.text, features="lxml")
    div = soup.find(tag_name, aclass)
    print(div)
    cprice = div.get_text().replace('₹', '').replace(',', '')
    daily_price.append(cprice)
    price_dates.append(now_time_date)
    return cprice


def sendmail():
    email_text = subject = "Product Price Alert"
    body = f"""\
    Hey,

    The price of the product has now reached our budget. You can buy it now.

    Product: {link}
    Price: {prod_price}$
    Date: {now_date}
    Time: {now_time}

    Best regards,
    Sachin's Development Bot
    """
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = "sachinofficial345@gmail.com"
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=email, password=email_pass)
    connection.sendmail(from_addr=email, to_addrs="sachinofficial345@gmail.com", msg=msg.as_string())
    print("Mail Success")
    connection.close()


if now_time == daily_checker_time:
    prod_price = price(tag_name, aclass)
    print(type(prod_price))
    product_price = int(prod_price)
    print(product_price)
    if product_price < target_amount:
        sendmail()
    else:
        print("Amount Has Not Yet Reduced")
else:
    print("Not the specified time.")

print(daily_price)
print(price_dates)
