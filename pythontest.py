
#SET-> 3 LAB EXAM
#agr kisi row se jo mising value hai usi ko uda dena hai
import pandas as pd


file_path = r"C:\Users\Surya Prakash\Downloads\AQI_Data (1).csv"

data = pd.read_csv(file_path)

print(data.head())  

#q1 solution
print(data.head(5))

#q2 solution
print(data.tail(6))


#q3 solution
print(data.describe())

#q4 solution
import numpy as np
city_mean_aqi = data.groupby('City')['AQI'].apply(np.mean)
print(city_mean_aqi)

city_mean_PM2= data.groupby('City')['PM2.5'].apply(np.mean)
print()
print(city_mean_PM2)

city_mean_pm10=data.groupby('City')['PM10'].apply(np.mean)
print()
print(city_mean_pm10)

#q5 solution
a=data['PM2.5']>100

c=data[a]
print(c)

print(c.shape[0])


