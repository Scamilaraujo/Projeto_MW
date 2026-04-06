#imports necessarios
from config.variaveis_ambiente import QUESTDB_HOST, QUESTDB_PORT, TABLE_NAME
from tratamento_dados.conexao_cliente import verificar_conexao
from tratamento_dados.status_internet import traduzir
from tratamento_dados.nome_cliente import atualizar_nomes
from banco_de_dados.questdb import enviar_para_questdb


import pandas as pd

#armazenando o caminho do .csv em uma variavel
CSV_PATH = "../data/questdb-usuarios-dataset.csv"

#lidando com possivel erro de carregamento do arquivo .csv
if (CSV_PATH != None):
    baseDeDados = pd.read_csv(CSV_PATH)
    print(f"CSV lido! {len(baseDeDados)} linhas | colunas: {list(baseDeDados.columns)}\n")
else:
    print("Erro: arquivo não encontrado.")


#transformando alguns dados. leia a descrição de cada arquivo para entender melhor
baseDeDados["conexaoCliente"] = baseDeDados["conexaoCliente"].apply(verificar_conexao) 
baseDeDados["statusInternet"] = baseDeDados["statusInternet"].apply(traduzir)
baseDeDados["nomeCliente"]    = baseDeDados["nomeCliente"].apply(atualizar_nomes)

#alguns logs
print("Transformações aplicadas. Prévia:")
print(baseDeDados.head(5).to_string(index=False))
print()

#chamando da função de enviar os dados para o questdb
enviar_para_questdb(baseDeDados, QUESTDB_HOST, QUESTDB_PORT, TABLE_NAME)