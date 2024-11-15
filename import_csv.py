import pandas as pd
from sqlalchemy import create_engine


df = pd.read_csv('NotaFiscal (1).xlsx - Plan 1.csv')


engine = create_engine('mysql+mysqlconnector://root:root123@localhost/db_loja')

df.to_sql('notafiscal', con=engine, if_exists='replace', index=False)

print("CSV importado com sucesso!")