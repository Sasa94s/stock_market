import pandas as pd
import numpy as np
import psycopg2
import sqlalchemy

engine = sqlalchemy.create_engine(
    'postgresql://postgres:5265104d@localhost:5432/stockmarket')

conn_string = "host='localhost' dbname='stockmarket' user='postgres' password='5265104d'"

conn = psycopg2.connect(conn_string)
n = input('Enter the id of companies')

df = pd.read_sql_query(
    '''select i.date ,i.open ,i.high ,i.low ,i.close ,i.adj_close ,i.volume ,c.name
    from dataset_information i 
    join dataset_company c
    on i.company_id=c.id
    where company_id = {}'''.format(n)  , conn, index_col='date')

df.index = pd.to_datetime(df.index)

print(df.head())
