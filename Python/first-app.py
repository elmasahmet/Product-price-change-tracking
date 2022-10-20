from email.mime import image
from itertools import product
from pickle import TRUE
import requests
from bs4 import BeautifulSoup
from send_email import sendMail
import time

url1="https://www.trendyol.com/xiaomi/miiiw-true-wireless-earphone-w200-bluetooth-kulaklik-p-299353004"


def checkPrice(url,paramPrice):

   headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
   }

   page = requests.get(url,headers=headers)

   htmlPage = BeautifulSoup(page.content,'html.parser')

   productTitle = htmlPage.find("h1", class_="pr-new-br").getText()

   price = htmlPage.find("span", class_="prc-dsc").getText()

   image = htmlPage.find("img",class_="base-product-image")

   convertedPrice = float(price.replace(",",".").replace(" TL",""))

   if(convertedPrice <= paramPrice):
      print("Ürün fiyatı düştü")
      htmlEmailContent=""""\
        <html>
        <head></head>
        <body>
        <h3>{0}</h3>
        <br/>
        {1}
        <br/>
        <p> Ürün Linki: {2}</p>
        </body>
        </html>
        """.format(productTitle,image, url)
      sendMail("#recipient email address", "Ürünün fiyatı düştü", htmlEmailContent)
   else:
     print("Ürün fiyatı düşmedi.")

while(TRUE):
 checkPrice(url1,150)
 time.sleep(3)
 