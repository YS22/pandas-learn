# --*-- coding:utf-8 --*--

import pandas as pd
from sqlalchemy import create_engine


con = create_engine('mysql+pymysql://username:passwd@ip:3306/dbname')

sql = """select * from depar_user """
data = pd.read_sql_query(sql,con)
