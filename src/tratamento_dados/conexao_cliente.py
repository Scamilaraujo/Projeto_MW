#---------------Trocar para nulo valores que não são um Num---------------
import pandas as pd

def verificar_conexao(valor):
    try:
        return float(valor)
    except (ValueError, TypeError):
        return pd.NA
