from getExchange import getExchange
from bs4 import BeautifulSoup
import re , json , datetime


class getVisaExchange(getExchange):
    def __init__(self):
        super().__init__()
        self.getPage()

    def getPage(self):
        def parseStr(inputStr):
            return re.sub('[\s*\r*\n*]' , '' , inputStr)

        getUrl = 'https://ferates.com/ajax/cards_table/visa/twd/%s' % ("{:%d.%m.%Y}".format(datetime.date.today()))
        super().getPage('https://ferates.com/valyuta/visa_mastercard/visa/twd')
        sessoinCookie = self.session.cookies.get_dict()
        cookieStr = ''
        for i in sessoinCookie:
            cookieStr = i+'='+sessoinCookie[i]
            
        headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
            'Connection': 'keep-alive',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip, deflate, br',
            'Cookie': cookieStr
            }
        rstHtml = ''
        
        try:
            rstHtml = json.loads(self.session.get(getUrl , headers=headers).text)['table']['all']
        except:
            return 'Error'

        soup = BeautifulSoup(rstHtml , 'html.parser')

        commonUseCurrency = ('usd' ,'hkd' ,'gbp' ,'cad' ,'sgd' ,'jpy' ,'eur','cny')
 
        for i in commonUseCurrency:
            currentTr = soup.find('tr' , {'id' : i})

            currencyInfo = currentTr.find('td' , {'class' : 'odd_row column_2'}).getText()
            currencyAsksNode = currentTr.find('td' , {'class' : 'column_5 last with-arrows'})
            self.exchangeDict['%s(%s)' % (currencyInfo , i.upper())] =parseStr(currencyAsksNode.find('div' , {'class':'value'}).getText())

    def calculate(self , currency , value):
        rst = super().calculate(currency , value)
        if rst:
            return 'NTD : %f' % (rst)
        else:
            return 'No Corrency found'

    @staticmethod
    def getWarrngMessige():
        return '(This exchange rate using \"Visa\" asking price)'


if __name__ == '__main__':
    a= getVisaExchange()
    print(a.calculate('USD' , 10))

        
        
