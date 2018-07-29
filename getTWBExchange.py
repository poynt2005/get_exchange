from getExchange import getExchange
from bs4 import BeautifulSoup
import re 


class getTWBExchange(getExchange):
    def __init__(self):
        super().__init__()
        self.getPage()

    def getPage(self):
        def parseStr(inputStr):
            return re.sub('[\s*\r*\n*]' , '' , inputStr)
        
        soup = BeautifulSoup(super().getPage('https://rate.bot.com.tw/xrt?Lang=zh-TW') , 'html.parser')
        currencyTr = soup.find('table').find('tbody').find_all('tr')

        for i in currencyTr:
            currencySellingRate = i.find('td' , {'data-table' : '本行即期賣出'}).getText()
            if not re.search('\-+' , currencySellingRate):
                self.exchangeDict[parseStr(i.find('div' , {'class' , 'hidden-phone print_show'}).getText())] = currencySellingRate

    def calculate(self , currency , value):
        rst = super().calculate(currency , value)
        if rst:
            return 'NTD : %f' % (rst)
        else:
            return 'No Corrency found'

    @staticmethod
    def getWarrngMessige():
        return '(This exchange rate using \"Bank of Taiwan\" sight selling rate)'


if __name__ == '__main__':
    a = getTWBExchange()
    print(a.calculate('USD' , 10))

