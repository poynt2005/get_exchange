import requests
from bs4 import BeautifulSoup
import re


class getExchange:
    def __init__(self):
        self.exchangeDict = {}
        self.session = requests.Session()
        self.getPage()

    def getPage(self):

        def parseStr(inputStr):
            return re.sub('[\s*\r*\n*]' , '' , inputStr)
        
        
        page = self.session.get('https://rate.bot.com.tw/xrt?Lang=zh-TW')

        soup = BeautifulSoup(page.text , 'html.parser')


        currencyTr = soup.find('table').find('tbody').find_all('tr')

        for i in currencyTr:
            currencySellingRate = i.find('td' , {'data-table' : '本行即期賣出'}).getText()
            if not re.search('\-+' , currencySellingRate):
                self.exchangeDict[parseStr(i.find('div' , {'class' , 'hidden-phone print_show'}).getText())] = currencySellingRate

    def calculate(self , currency , value):
        currency = currency.upper()
        for k in self.exchangeDict:
            if not re.search(currency , k):
                continue
            else:
                return 'NTD : {}'.format(float(value) * float(self.exchangeDict[k]))
        return 'No Corrency found'
