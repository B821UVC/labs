import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
import openpyxl
df = pd.read_csv("датасет-1.csv", sep=';')

df['price']=df['price'].str.replace(',','.')
df['price']=df['price'].astype(float)
print(df)
reg = linear_model.LinearRegression()
reg.fit(df[['area']],df.price)
plt.scatter(df.area,df.price,color='red') # в качестве аргумента указываем название столбцов
plt.plot(df.area, reg.predict(df[['area']]))
plt.xlabel('площадь(кв.м.)') # подпишем координатные оси 
plt.ylabel('стоимость(млн.руб)')
plt.show()

#for predict_price.csv

pred = pd.read_csv("prediction_price.csv", sep=';')

p = reg.predict(pred)

pred['predicted_price'] = p
print(pred)

pred.to_excel('new.xlsx', index=False)