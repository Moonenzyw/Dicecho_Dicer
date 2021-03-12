# 用于和数据库交互，获取玩家卡等信息

import os
import sqlite3

DB_FILE=os.path.join('data','dicer','dicer.db')

def py2sql(value)->str:
    if isinstance(value,str):
        result=f'"{value}"'
    else:
        result=str(value)
    return result

def create_db(sql = ""):
    if not os.path.exists(DB_FILE):
        os.makedirs(os.path.join('data','dicer'))
    conn=sqlite3.connect(DB_FILE)
    cur=conn.cursor()
    # 用户数据
    cur.execute(sql)
    conn.commit()
    conn.close()

def update_db(table_name:str,columns:dict,condition:dict)->bool:
    create_db()
    try:
        conn=sqlite3.connect(DB_FILE)
        cur=conn.cursor()
        sql=f"UPDATE {table_name} SET "
        for i,key in enumerate(columns.keys()):
            if i:sql+=','
            sql+=f"{key} = {py2sql(columns[key])}"
        sql+=" WHERE "
        for i,key in enumerate(condition.keys()):
            if i:sql+=' AND '
            sql+=f"{key} = {py2sql(condition[key])}"
        cur.execute(sql)
        conn.commit()
        conn.close()
        return True
    except:
        return False

def insert_db(table_name:str,columns:dict)->bool:
    create_db()
    try:
        conn=sqlite3.connect(DB_FILE)
        cur=conn.cursor()
        sql=f"INSERT INTO {table_name} ("
        for i,key in enumerate(columns.keys()):
            if i:sql+=','
            sql+=key
        sql+=') VALUES ('
        for i,key in enumerate(columns.keys()):
            if i:sql+=','
            sql+=py2sql(columns[key])
        sql+=')'
        cur.execute(sql)
        conn.commit()
        conn.close()
        return True
    except:
        return False

def select_db(table_name:str,columns:tuple,condition:dict):
    create_db()
    try:
        conn=sqlite3.connect(DB_FILE)
        cur=conn.cursor()
        sql="SELECT "
        for i,value in enumerate(columns):
            if i:sql+=','
            sql+=value
        sql+=f' FROM {table_name} WHERE '
        for i,key in enumerate(condition.keys()):
            if i:sql+=' AND '
            sql+=f"{key} = {py2sql(condition[key])}"
        cur.execute(sql)
        return cur.fetchall()[0]
        conn.close()
    except:
        return False

def delete_db(table_name:str,condition:dict):
    create_db()
    try:
        conn=sqlite3.connect(DB_FILE)
        cur=conn.cursor()
        sql=f'DELETE FROM {table_name} WHERE '
        for i,key in enumerate(condition.keys()):
            if i:sql+=' AND '
            sql+=f"{key} = {py2sql(condition[key])}"
        cur.execute(sql)
        conn.commit()
        conn.close()
        return True
    except:
        return False

# 测试
if __name__=='__main__':
    insert_db("qqgroup", {"id" : 224682086, "name" : "骰娘测试群"})
    result = select_db("qqgroup", ("name",), {"id" : 224682086})