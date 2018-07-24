import requests
from bs4 import BeautifulSoup
import re

class get_exchange :
    def __init__(self):
        self.exchange_dict = {'美金 USD': ' ' , '港幣 HKD' : ' ' , '馬來幣 MYR' : ' ' , '英鎊 GBP' : ' ' , '澳幣 AUD' : ' ' , '加拿大幣 CAD' : ' ' , '新加坡幣 SGD' : ' ' , '瑞士法郎 CHF' : ' ' , '日圓 JPY' : ' ' , '瑞典幣 SEK' : ' ' , '紐元 NZD' : ' ' , '泰幣 THB' : ' ' , '菲國比索 PHP' : ' ' , '印尼幣 IDR' : ' ' , '歐元 EUR' : ' ' , '韓元 KRW' : ' ' , '人民幣 CNY' : ' ' , '越南盾 VND' : ' ' , '比特幣 BTC' : ' '}

    def getInfoFromBOT(self):
        re = requests.session()
        res = re.get('https://fctc.bot.com.tw/Purchase/WarningPage#')
        
        soup = BeautifulSoup(res.text,'html.parser')
        sessionToken =  soup.input.get('value')
        payload = {'__RequestVerificationToken' : sessionToken}
        
        res2 = re.post('https://fctc.bot.com.tw/Purchase/SelectCurrencyBank' , data = payload)
        
        soup2 = BeautifulSoup(res2.text,'html.parser')

        for i in soup2.find_all('div', {'class' : 'Exchange rate'}) :
            if(i.find('p' , {'class' : 'Country_USD'})) : 
                self.exchange_dict['美金 USD'] =  i.find('p' , {'class' : 'Country_USD'}).findNext('p' , {'class' : 'number'}).string
            if(i.find('p' , {'class' : 'Country_HKD'})) : 
                self.exchange_dict['港幣 HKD'] =  i.find('p' , {'class' : 'Country_HKD'}).findNext('p' , {'class' : 'number'}).string
            if(i.find('p' , {'class' : 'Country_MYR'})) : 
                self.exchange_dict['馬來幣 MYR'] =  i.find('p' , {'class' : 'Country_MYR'}).findNext('p' , {'class' : 'number'}).string
            if(i.find('p' , {'class' : 'Country_GBP'})) : 
                self.exchange_dict['英鎊 GBP'] =  i.find('p' , {'class' : 'Country_GBP'}).findNext('p' , {'class' : 'number'}).string
            if(i.find('p' , {'class' : 'Country_AUD'})) : 
                self.exchange_dict['澳幣 AUD'] =  i.find('p' , {'class' : 'Country_AUD'}).findNext('p' , {'class' : 'number'}).string
            if(i.find('p' , {'class' : 'Country_CAD'})) : 
                self.exchange_dict['加拿大幣 CAD'] =  i.find('p' , {'class' : 'Country_CAD'}).findNext('p' , {'class' : 'number'}).string
            if(i.find('p' , {'class' : 'Country_SGD'})) : 
                self.exchange_dict['新加坡幣 SGD'] =  i.find('p' , {'class' : 'Country_SGD'}).findNext('p' , {'class' : 'number'}).string
            if(i.find('p' , {'class' : 'Country_CHF'})) : 
                self.exchange_dict['瑞士法郎 CHF'] =  i.find('p' , {'class' : 'Country_CHF'}).findNext('p' , {'class' : 'number'}).string
            if(i.find('p' , {'class' : 'Country_JPY'})) : 
                self.exchange_dict['日圓 JPY'] =  i.find('p' , {'class' : 'Country_JPY'}).findNext('p' , {'class' : 'number'}).string
            if(i.find('p' , {'class' : 'Country_SEK'})) : 
                self.exchange_dict['瑞典幣 SEK'] =  i.find('p' , {'class' : 'Country_SEK'}).findNext('p' , {'class' : 'number'}).string
            if(i.find('p' , {'class' : 'Country_NZD'})) : 
                self.exchange_dict['紐元 NZD'] =  i.find('p' , {'class' : 'Country_NZD'}).findNext('p' , {'class' : 'number'}).string
            if(i.find('p' , {'class' : 'Country_THB'})) : 
                self.exchange_dict['泰幣 THB'] =  i.find('p' , {'class' : 'Country_THB'}).findNext('p' , {'class' : 'number'}).string
            if(i.find('p' , {'class' : 'Country_PHP'})) : 
                self.exchange_dict['菲國比索 PHP'] =  i.find('p' , {'class' : 'Country_PHP'}).findNext('p' , {'class' : 'number'}).string
            if(i.find('p' , {'class' : 'Country_IDR'})) : 
                self.exchange_dict['印尼幣 IDR'] =  i.find('p' , {'class' : 'Country_IDR'}).findNext('p' , {'class' : 'number'}).string
            if(i.find('p' , {'class' : 'Country_EUR'})) : 
                self.exchange_dict['歐元 EUR'] =  i.find('p' , {'class' : 'Country_EUR'}).findNext('p' , {'class' : 'number'}).string
            if(i.find('p' , {'class' : 'Country_KRW'})) : 
                self.exchange_dict['韓元 KRW'] =  i.find('p' , {'class' : 'Country_KRW'}).findNext('p' , {'class' : 'number'}).string
            if(i.find('p' , {'class' : 'Country_CNY'})) : 
                self.exchange_dict['人民幣 CNY'] =  i.find('p' , {'class' : 'Country_CNY'}).findNext('p' , {'class' : 'number'}).string
            if(i.find('p' , {'class' : 'Country_VND'})) : 
                self.exchange_dict['越南盾 VND'] =  i.find('p' , {'class' : 'Country_VND'}).findNext('p' , {'class' : 'number'}).string
                
    def getInfoFromCoinmill(self):
        res = requests.get('https://zt.coinmill.com/BTC_TWD.html')
        soup = BeautifulSoup(res.text,'html.parser')
        data = soup.find(string = re.compile('1.0000')).findNext('td').string.split('\n')[1].split(',')
        self.exchange_dict['比特幣 BTC'] = float(data[0] + data[1])

    def display_exchange(self):
        for i in self.exchange_dict :
            print(i ,'\t',':',self.exchange_dict[i])

    def calculate(self,currency,value):
        Currency_found = 0
        for j in self.exchange_dict : 
            exchange_dictionary_key = str(j).split()[1]
            if currency == exchange_dictionary_key :
                number = float(self.exchange_dict[j])
                #print('NTD : ' , number * value , '\n')
                Currency_found = 1
                return 'NTD : {}'.format(number * value)
        if Currency_found == 0:
            #print('No Corrency found\n')
            return 'No Corrency found'

def main():
    exchange = get_exchange()
    exchange.getInfoFromBOT()
    exchange.getInfoFromCoinmill()
    exchange.display_exchange()
    while True :
        i = input('insert Currency name abbreviation to convert to NTD , insert "0" to exit (Ex : USD 10): ')
        if i == '0':
            break
        else :
            tmp = i.split()
            if len(tmp) == 2:
                current_currency = str(tmp[0]).upper()

                try : 
                    if(isinstance(float(current_currency),float)):
                        print('Input error , insert again\n')
                        continue
                except :
                    pass
            
                try :
                    current_value = float(tmp[1])
                except:
                    print('Input error , insert again\n')
                    continue
            
                output_message = exchange.calculate(current_currency,current_value)
                print(output_message)
            
            else :
                print('Input error , insert again\n')
                continue

if __name__ == '__main__':
    main()
