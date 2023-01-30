import sys
sys.path.append("..") # add the module to path

from msfinance.Instrument import Instrument
from datetime import datetime

from msfinance.COMMON import COMMON
from msfinance.XU100 import XU100
from msfinance.XU030 import XU030

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import sklearn.metrics as metrics
from sklearn.metrics import r2_score

start_date = datetime(2022,1,3)
end_date = datetime(2023,1,27)

eregli = Instrument(XU100.EREGL)
eregli.getDataStartToEnd( start_date, end_date )

cds_6m = Instrument('CDS_6M')
cds_6m.getDataFromFile('./test_files/cds_6m.csv')

cds_1y = Instrument('CDS_1Y')
cds_1y.getDataFromFile('./test_files/cds_1y.csv')

usd_try = Instrument(COMMON.USD_TRY)
usd_try.getDataStartToEnd(start_date ,end_date)

# bist_sust = Instrument("BIST_SUST")
# bist_sust.getDataFromFile('./test_files/bist_sust.csv')


for stock_name in XU030:
    stock = Instrument(stock_name)
    stock.getDataStartToEnd( start_date, end_date )

    total_df = stock.getData()[["Close"]].join(usd_try.getData()[["Close"]] , lsuffix= '_eregl' , rsuffix='_usdtry')
    total_df = total_df.join(cds_6m.getData()[['Price']] , rsuffix='_cds6m')
    total_df = total_df.join(cds_1y.getData()[['Price']] , rsuffix='_cds1y')
    total_df.columns = ['Target' , 'usdtry','cds6m','cds1y']
    total_df.fillna(method='bfill' , inplace= True)

    #print(total_df)
    #print(total_df.info())
    #print(total_df[total_df['cds1y'].isnull()])
    # print(usd_try.getData().head())
    # print(stock.getData().head())

    total_df.reset_index(inplace=True)
    #print(total_df)


    X = total_df[["usdtry" , 'cds6m','cds1y']]
    y=total_df['Target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

    linear_model = LinearRegression()
    linear_model.fit(X_train , y_train)
    y_predict = linear_model.predict(X_test)

    print( stock_name ,r2_score(y_test , y_predict) )

    mae = metrics.mean_absolute_error(y_test, y_predict)
    mse = metrics.mean_squared_error(y_test, y_predict)
    rmse = np.sqrt(mse)

    # actual_minus_predicted = sum((y_test - y_predict)**2)
    # actual_minus_actual_mean = sum((y_test - y_test.mean())**2)
    # r2 = 1 - actual_minus_predicted/actual_minus_actual_mean
    # print('R²:', r2)