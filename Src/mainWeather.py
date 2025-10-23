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

##Construir o modelo de rede neural
modelo = keras.Sequential([
    keras.layers.Dense(8, activation = 'relu', input_shape = [1]),
    keras.layers.Dense(1)
])
modelo.compile(optimizer = 'adam', loss = 'mse')

#Treinar o modelo
modelo.fit(h, a, epochs = 500, verbose = 0)
