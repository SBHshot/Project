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
    test_result = pd.read_sql(test_query, engine)
    # timestamp處理,避免出現太多0
    test_result['Due_Date'] = test_result['Due_Date'].astype(str)
    test_result['Suggest_Date'] = test_result['Suggest_Date'].astype(str)
    # 將dataframe標題儲存成tuple
    # for <thead>
    heading = list(test_result)
    heading.insert(0, '')
    heading = tuple(heading)
    # 儲存dataframe內容
    # for <tbody>
    content = list(test_result.to_records())
    content = tuple(content)
    return render_template('index.html', headings=heading, contents=content)


if __name__ == "__main__":  # 如果以主程式執行
    app.run()  # 立刻啟動伺服器
