import sys  
import datetime 
import pandas as pd
from questdb.ingress import Sender, IngressError 

def enviar_para_questdb(df: pd.DataFrame, host: str, port: int, table_name: str) -> None:
    
    print(f"Enviando para QuestDB ({host}:{port}) ...")

    try:
        
        with Sender.from_conf(f"tcp::addr={host}:{port};") as sender:

        
            now = datetime.datetime.utcnow()

            for i, row in df.iterrows():

                columns = {}

                for col in df.columns:
                    val = row[col]  

                    try:
                        if pd.isna(val):
                            continue 
                    except (TypeError, ValueError):
                        pass

                    if isinstance(val, float) and val == int(val):
                        columns[col] = int(val)
                    else:

                        columns[col] = val

                sender.row(table_name, symbols={}, columns=columns, at=now)

            sender.flush()

        print(f"{len(df)} registros enviados para a tabela '{table_name}'!")

    except IngressError as e:
        print(f"[ERRO] QuestDB IngressError: {e}")
        sys.exit(1)  
   
    except Exception as e:
        print(f"[ERRO] Erro inesperado: {e}")
        sys.exit(1)