import yfinance as yf 
import matplotlib.pyplot as plt 
import pandas 
import csv


q="-"*20

def welcome_screen ():
    print ('Hello!!!\n'+ q)

    name= input('Input your name: ')
    surname = input('Your surname: ')

    print(q)
    print (f'Glad to see you {name} {surname} \n' + q)

def inp_T ():
    #принимает ввод тикера 
    print ("1.Московская биржа \n2.Американская биржа \n"+ q )
    chs=int(input ("1 or 2 \n"))
    if chs == 1:
        tic = str(input ("Введите тикер, например GAZP/MOEX/SBER \n"))
        tic= tic + '.ME'
    else: 
        tic = str(input ("Введите тикер, например TSLA/AAPL/AMZN \n"))

    data = yf.Ticker(tic)
    return data

def request_t (a):
    price= a.history(period='5y')
    x = price['Close'].pct_change()
    returns = (x + 1).cumprod()
    returns.plot()
    plt.savefig('plo1t.png')
    
def comp_inf(a):
    print(a.dividends)
    print (a.splits)
    #print (a.balance_sheet) 
    print (a.cashflow)




def main ():
    a= inp_T()
    print ("Нужна информация о компании? \ny/n")
    b=input ()
    if b == "y":
        comp_inf(a)
    elif b =="n" :
        print ('тогда ладно')
    else:
        print ('жопа')
    request_t(a)

main()