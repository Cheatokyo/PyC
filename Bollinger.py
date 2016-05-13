# Bollinger Band exercise
"""
Created on Sun Apr  3 10:06:35 2016

@author: Chea
"""

import os
import pandas as pd
import matplotlib.pyplot as plt


def symbol_to_path(sym,base_dir='Data'):
    p =  os.path.join(base_dir,'{}.csv'.format(str(sym)))
    return p

def load_prices():
    start_date = '2015-04-01'
    end_date = '2016-04-01'
    dates=pd.date_range(start_date,end_date)
    
    df1=pd.DataFrame(index=dates)


    symbols=['KOSPI2']
    for sym in symbols:
        df_temp=pd.read_csv(symbol_to_path(sym),index_col='Date',parse_dates=True,
                         na_values=['NaN'])
                         
          
        df_temp=df_temp.rename(columns={'PX_LAST':sym})
        
        df1=df1.join(df_temp,how='inner')
        
    df1=df1.sort(axis=0)   
    return df1
    

if __name__ == '__main__':
    
    sym = 'KOSPI2'
    period = 20
    Price = load_prices()
    Smov =   pd.rolling_mean(Price,window=period)
    Svol =   pd.rolling_std(Price,window=period)
    Uband = Smov+2*Svol
    Dband = Smov-2*Svol
 
    Yield = Price.copy()
    Yield[1:] = (Price[1:].values/Price[:-1].values)-1
    Yield.ix[0]=0
  
    plt.plot(Price,label='Close')  
    plt.plot(Smov,label=str(period) +'D MAV')
    plt.plot(Uband,label='Upper band')
    plt.plot(Dband, label='Lower band')

    plt.title('MAV and BOLLINGER')
    plt.legend()
    plt.show()
    
    plt.plot(Yield,label='Yield')  
    plt.title('1D change')
    plt.legend()
    plt.show()