from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

my_email = "dipstha393@gmail.com"
password = "hkct tuav brka zmzv"

send_email = "dipeshsth00@gmail.com"

url = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Brave/1.50.114",
    "Accept-Language": "en-US,en;q=0.8"
}
response = requests.get(url, headers=headers)
response.raise_for_status()

website_html = response.text

soup = BeautifulSoup(website_html, "lxml")

BUY_PRICE = 200

title = soup.find(id="productTitle").get_text().strip()
price = soup.find(class_="a-offscreen").getText()

price_without_currency = price.split('$')[1]

price_as_float = float(price_without_currency)

if price_as_float < BUY_PRICE:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=send_email,
                            msg=f"subject:Amazon Price Alert!\n\n{title} is now {price}\n{url}".encode("utf-8")
                            )
