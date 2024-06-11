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
        pass


device = PriceTracer(url="https://www.amazon.nl/Apple-AirPods-generatie-MagSafe-oplaadcase-USB%E2%80%91C/dp/B0CHWZ9TZS?ref_=Oct_DLandingS_D_f7afbe79_0")
print(device.product_title())