from get_exchange import *
from tkinter import *


class GUI(get_exchange):
    def __init__(self , win):
        super().__init__()
        super().getInfoFromBOT()
        super().getInfoFromCoinmill()

        self.win = win
        
        self.win.title('Exchange Calculate')
        
        self.win.resizable(0,0)
        
        for i in self.exchange_dict:
            exchange_message = '{} : {}'.format(i,self.exchange_dict[i])
            Label(self.win , text = exchange_message).grid()
        
        Label(self.win , text = '\nInsert Curren$y abbreviation to convert to NTD (Ex : USD 10)').grid()
        
        self.entry = Entry(self.win)
        self.entry.grid()
        self.entry.focus()       
        
        var = StringVar()
        result = Label(self.win , textvariable = var).grid()
        
        self.button = Button(self.win , text = 'Calculate Exchange' , command = lambda : self.callback(var , self.entry.get())).grid()

        self.win.bind('<Return>' , lambda x: self.callback(var , self.entry.get()))
        
        Frame(self.win , width = 300 , height = 50).grid()
        
        
        
    def callback(self,var,user_input):
        tmp = user_input.split()
        if len(tmp) == 2:
            flag = 0
            current_currency = str(tmp[0]).upper()

            try : 
                if(isinstance(float(current_currency),float)):
                    output_message = 'Input error , insert again'
                    flag = 1
            except :
                pass
            
            try :
                current_value = float(tmp[1])
            except:
                output_message = 'Input error , insert again'
                flag = 1
            if not flag == 1:
                output_message = super().calculate(current_currency,current_value)
        else :
            output_message = 'Input error , insert again'
        
        var.set(output_message)


        


