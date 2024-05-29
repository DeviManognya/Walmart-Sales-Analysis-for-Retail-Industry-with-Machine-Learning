import numpy as np
from numpy.core.fromnumeric import size
import pandas as pd
from sklearn.model_selection import train_test_split
from flask import Flask,render_template,request
import pickle
import datetime as dt
import calendar
import os

app=Flask(__name__)

loaded_model=pickle.load(open(r'C:\Users\srinu\Desktop\Flask project\rf_model.pkl','rb'))
fet=pd.read_csv(r'C:\Users\srinu\Desktop\Flask project\merged_data.csv')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
  print("Request Headers:", request.headers)
  print("Form Data:", request.form)
  store=request.form.get('store')
  dept=request.form.get('dept')
  date=request.form.get('date')
  isHoliday=request.form['isHolidayRadio']
  size=request.form.get('size')
  temp=request.form.get('temp')
  return render_template('index.html')

  d=dt.datetime.strptime(date,'%Y-%m-%d')
  year=(d.year)
  month=d.mont
  month_name=calendar.month_name[month]
  print("year=",type(year))
  print("year val=",year,type(year),month)
  X_test=pd.DataFrame({'Store':[store],'Dept':[dept],'Size':[size],'temperature':   [temp],'CPI':[212],'MarkDown4':[2050],'IsHoliday':[isHoliday],'Type_B':[0],'Type_C':[1],'month':[month],'year':[year]})
  print("X_test=",X_test.head())
  print("type of X_test=",type(X_test))
  print("predict=",store,dept,date,isHoliday)

  y_pred=loaded_model.predict(X_test)
  output=round(y_pred[0],2)
  print("predicted=",output)
  return render_template('index.html',output=output,store=store,dept=dept,month_name=month_name,year=year)

port=os.getenv('VCAP_APP_PORT','8080')


if __name__=="__main__":
  app.secret_key=os.urandom(12)
  app.run(debug=False,host="0.0.0.0",port=port)