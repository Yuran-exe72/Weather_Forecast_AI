#Importando Bibliotecas necessárias
import numpy as np
import pandas as pd
from tensorflow import keras
import matplotlib.pyplot as plt

#Carregar dados do modelo
dados = pd.read_csv('Data/weather_data.csv')
dados.columns = ['Data', 'Temperatura']

#Preparar as temperaturas h(Hoje) e a(Amanhã)
temps = dados['Temperatura'].values.astype(float)
h = temps[:-1].reshape(-1, 1)
a = temps[1:]
