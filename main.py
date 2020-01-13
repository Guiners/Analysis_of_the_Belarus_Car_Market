import pandas as pd

import os
os.getcwd()
os.listdir()

os.chdir('/Users/Robert/Desktop/Studia/III SEMESTR/Analiza i wizualizacja danych')

file = 'cars.csv'
data = pd.read_csv(file)
#help(pd.read_csv)#

print(data.columns)