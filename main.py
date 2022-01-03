import pandas as pd
import numpy as np

dataS = pd.read_csv('schoolProject\dataS.csv')
# print(dataS.head())
tempS = dataS.iloc[:, [4]]
# print(tempS)

dataD = pd.read_csv('schoolProject\dataD.csv')
# print(dataD.head())
tempD = dataD.iloc[:, [4]]
# print(tempD)

dtemp = {"average": round(tempD.mean()["temp"], 2), "max": round(tempD.max()["temp"], 2), "min": round(tempD.min()["temp"], 2)}
stemp = {"average": round(tempS.mean()["temp"], 2), "max": round(tempS.max()["temp"], 2), "min": round(tempS.min()["temp"], 2)}
print("Average temperature in the city of Delhi: ", dtemp["average"])
print("Average temperature in the city of Sikkim: ", stemp["average"])
print("Difference in AVERAGE temperature between the two cities: ", dtemp["average"] - stemp["average"])
print()
print("Maximum temperature in the city of Delhi: ", dtemp["max"])
print("Maximum temperature in the city of Sikkim: ", stemp["max"])
print("Difference in MAXIMUM temperature between the two cities: ", dtemp["max"] - stemp["max"])
print()
print("Minimum temperature in the city of Delhi: ", dtemp["min"])
print("Minimum temperature in the city of Sikkim: ", stemp["min"])
print("Difference in MINIMUM temperature between the two cities: ", dtemp["min"] - stemp["min"])



