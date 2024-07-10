import requests
from bs4 import BeautifulSoup


class PriceTracer:
    def __init__(self, url):
        self.url = url
        self.user_agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0"}
        self.response = requests.get(url=self.url, headers=self.user_agent).text
        self.soup = BeautifulSoup(self.response, "lxml")

    def product_title(self):
        title = self.soup.find("span",{"id":"productTitle"})
        if title is not None:
            return title.text.strip()
        else:
            return "Tag not found"

    def product_price(self):
        price = self.soup.find("span", {"class": "a-price-whole"})
        if price is not None:
            return price.text.strip()
        else:
            return "Price not found"


device = PriceTracer(url="https://www.amazon.in/Samsung-Phantom-Storage-Additional-Exchange/dp/B0B8S83RPT/ref=sr_1_1_sspa?crid=1NXN3DOS62IP7&dib=eyJ2IjoiMSJ9.K2HSxXAyxk0Mc59ScRq1TmasuFDBurI2zbca_bLACoi3OEPnIIVM2s-Bu0jmULSf1_JpFL3tySRzZQQZnFL5EvawvVzmzCdtBAERlnzw58AopntVKWr6PVtk5yvo3HqkZbzmHXm1ujZZn3NcnSzKyc2zB1Ysg5cdcOj7l2XtveFI3OwLKiEn5XJ2slrBkpt7cHQC7HoE-VOgvvtL9RXNl9p1vJvBfzrZuGEKal_AAEvcdAjSxdSsOvaT1ulDLmw2AQthjotfGlglsVFD87kdkpZZaUET3339BKFiOLPT9uw.5uE5v5SGgGm5wcZufE0ctcQDcVOsezFU-6ZLlYS3Qf0&dib_tag=se&keywords=samsung+5g+mobile&qid=1720442984&s=electronics&sprefix=sa%2Celectronics%2C254&sr=1-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1")
# device = PriceTracer(url="https://www.amazon.nl/Apple-AirPods-generatie-MagSafe-oplaadcase-USB%E2%80%91C/dp/B0CHWZ9TZS?ref_=Oct_DLandingS_D_f7afbe79_0")
print(device.product_title())
print(device.product_price())