import re , requests
from bs4 import BeautifulSoup

class getExchange:
    def __init__(self):
        self.exchangeDict = {}
        self.session = requests.Session()
        
    def getPage(self , url):

        headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
            }
        page = self.session.get(url , headers=headers)
        
        return page.text


    def calculate(self , currency , value):
        currency = currency.upper()
        for k in self.exchangeDict:
            if not re.search(currency , k):
                continue
            else:
                return float(value) * float(self.exchangeDict[k])
        return False

