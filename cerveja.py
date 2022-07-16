import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def main():
    data = pd.read_csv("Dados/Consumo_cerveja.csv", sep=";")
    print("\n Resumo de medidas descritivas do dataset: \n")
    print(data.describe().round(2))
    print("\n Correlação entre as variáveis: \n")
    print(data.corr().round(4))

main()
