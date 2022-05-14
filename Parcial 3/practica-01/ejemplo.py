##Importar datos.
import pandas as pd
import csv


data = pd.read_csv('iris.csv')
print(data.head()) #Muestra los primeros cinco registros.