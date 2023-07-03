import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv

load_dotenv()

Dataset = os.getenv("Airbnb")

Read_Dataset = pd.read_csv(Dataset)

#Es una buena prcativa hacer una copia del dataset original para evitar modificarlo
Dataset_Airbnb = Read_Dataset.copy()

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

PrintColumnTypes(categorias, numericas)