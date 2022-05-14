#Librerias  necesarias
from tokenize import group
import matplotlib.pyplot as plt
import pandas as pd
import csv

#leer datos desde csv.
data = pd.read_csv('surveys.csv')
#use head() to see the first 5 rows of the data.
print(data.head())
#show all data
print(data)

#Explorando los datos del censo de las especies.
#using type() to see the data type of each column.
type(data)

#usinf data.dtypes to see the data type of each column.
data.dtypes

#using data.columns to see the column names.
data.columns

#using data.shape to see the number of rows and columns.
data.shape

#when you put a n (number) in head(), it shows the first n rows.
data.head(15)

#using data.tail to see the last 5 rows.

data.tail()

###Calculando estadísticas.
#Show columns from data.
data.columns

#using 'unique' to see the number of unique values in each column.
pd.unique(data['species_id'])

#Create a list of IDS.
site_names = pd.unique(data['plot_id']).tolist()

###Grupos en pandas.
#Using weith() to see the weight of each species.
data['weight'].describe()

#Metricas en particular.
data['weight'].min()
data['weight'].max()
data['weight'].mean()
data['weight'].std()
data['weight'].count()

#Using groupby() to see make a group of species by sex.
grouped_data = data.groupby('sex')

#Usign describe to show descriptive stadistics.

#Estadisticas para todas las columnas numericas por sexo.
grouped_data.describe()

#Regresa la media de cada columna numerica por sexo.
grouped_data.mean()
#Get the number of columns of both sexs.
grouped_data.mean().shape

#
grouped_data2 = data.groupby(['plot_id', 'sex'])
grouped_data.mean()

###Creando estadísticas de conteos.

species_count =  data.groupby('species_id')['record_id'].count()
print(species_count)

#Using DO
data.groupby('species_id')['record_id'].count()['DO']
 
#Funciones basicas de matermaticas.
#Multiplicar todos los valores por 2.
data['weight'] * 2

#Graficacion de datos.
#Using matplotlib to plot the data.

my_plot = species_count.plot(kind='bar')
#Se debe usar plt.show() para mostrar el grafico.

total_count = data.groupby('plot_id')['record_id'].nunique()
my_plot = total_count.plot(kind='bar')


d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
pd.DataFrame(d)
my_df = pd.DataFrame(d)
my_plot = my_df.plot(kind='bar', stacked=True, title='The little of my graph')


