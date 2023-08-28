import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv

import time

load_dotenv()

Dataset = os.getenv("Airbnb")

Read_Dataset = pd.read_csv(Dataset)

#Es una buena practica hacer una copia del dataset original para evitar modificarlo
Dataset_Airbnb = Read_Dataset.copy()

Dataset_Airbnb.head()

def Main():

    print(Dataset_Airbnb.head().columns)

    print(Dataset_Airbnb.info())

    #Separar nuestras funciones en numéricas y categóricas desde el principio es útil para el análisis exploratorio de datos.

    categorias = Dataset_Airbnb.select_dtypes(include = ["object"])
    print(categorias)

    numericas = Dataset_Airbnb.select_dtypes(exclude = ["object"])

    print(numericas)


def PrintColumnTypes(categorias, numericas):

    print("Columnas no numericas: ")

    for i in categorias:
        print(i)
    print("")

    print("Columnas numericas: ")

    for i in numericas:
        print(i)

# Dataset_Airbnb.isna()


def Missing_Data(Dataset_Airbnb):
    # vamos a ver cuantos datos faltantes tenemos

    print("missing data: ")

    total = 0
    for i in Dataset_Airbnb.columns:
        missing_value = Dataset_Airbnb[i].isnull().sum()
        total += missing_value

        if missing_value != 0:
            print(f"{i} => {Dataset_Airbnb[i].isnull().sum()}")

    if total == 0:
        print("No hay datos faltantes")

def Porc_missing(Dataset_Airbnb):

    for i in Dataset_Airbnb.columns:

        porcentaje = Dataset_Airbnb[i].isna().mean() * 100

        if porcentaje != 0:
            print("{} => {}%".format(i, round(porcentaje, 2)))

Porc_missing(Dataset_Airbnb)

# plt.figure(figsize=(10, 6))

# sns.heatmap(Dataset_Airbnb.isnull(), yticklabels=False, cmap="viridis", cbar=False)

#Si deseas mantener la ventana del gráfico abierta hasta que la cierres manualmente, puedes 
# utilizar el método plt.show(block=True) en lugar de plt.show(). Esto bloqueará la ejecución del programa hasta que la ventana del gráfico se cierre.
plt.show(block=True)


# Missing_Data(Dataset_Airbnb)

# PrintColumnTypes(categorias, numericas)