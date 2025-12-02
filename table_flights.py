import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import math 

url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/flights.csv'

flight_table = pd.read_csv(url)
#print(flight_table.head())

media_passageiros = flight_table.groupby('year')['passengers'].mean().reset_index()

media_passageiros.columns = ['year', 'media passageiros']

print(media_passageiros)

plt.figure(figsize=(12,6))
plt.bar(media_passageiros['year'], media_passageiros['media passageiros'])

plt.xlabel("Ano")
plt.ylabel('Média de passageiros')
plt.title('Média de passageiros por ano')

plt.tight_layout()

plt.show()