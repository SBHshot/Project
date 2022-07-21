from cProfile import label
from cgi import test
from http import server
from msilib.schema import tables
from sqlite3 import connect
from unicodedata import name
from sqlalchemy import create_engine, inspect, text
from sqlalchemy.orm import sessionmaker
from flask import Flask, render_template, Request
from flask_pagination import Pagination
import pandas as pd
import pymssql
import db

app = Flask(__name__)

engine = create_engine(
    'mssql+pymssql://mtbtestee:Aa12366@@TAWSQLDBA01\TAMSSDBA01/MTB_TEST_EE')
DBSession = sessionmaker(bind=engine)


@app.route('/', methods=['GET', 'POST'])
def home():

    db_query = 'select * from PM_calendar_rawdata WITH (NOLOCK)'
    test_query = 'select * from test WITH (NOLOCK)'
    inspector = inspect(engine)
    db_result = pd.read_sql(db_query, engine).drop_duplicates()
    db_result["NOTE"] = ""
    db_result.to_sql('test', engine, if_exists='replace', index=False)
    # 從資料庫讀取資料
    test_result = pd.read_sql(test_query, engine)
    print(list(test_result))
    heading = list(test_result)
    heading.insert(0, '')
    heading = tuple(heading)
    print(heading)
    test_result_no_header = test_result.
    # str -> list
    # table = tuple([test_result.to_html(classes='data', header='false')])
    print(type(test_result_no_header))
    content = []
    for row in test_result_no_header.iterrows():
        content.append(row)
    content = tuple(content)
    print(content)
    return render_template('index.html', headings=heading, contents=content)
    # headings = tuple(list(test_result))


if __name__ == "__main__":  # 如果以主程式執行
    app.run()  # 立刻啟動伺服器
