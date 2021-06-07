from flask import Flask, render_template,jsonify
from flask_cors import CORS
import sqlite3

class TatekanData:
    def __init__(self, title, image, description, pos_x, pos_y):
        self.title = title
        self.image = image
        self.description = description
        self.pos_x = pos_x
        self.pos_y = pos_y

    # 画像ファイルのファイル名を生成
    # 
    def createFileName(db_cur, uploaded_name):
        fname = list(db_cur.execute("select count(*) from tatekan;"))[0]
        return fname + "." + (uploaded_name.split("."))[-1]

    # データベースに登録
    def insertToDB(db_cur, tatekanData, table_name):
        sql = "insert into " + table_name + " values(?, ?, ?, ?, ?);"
        db_cur.execute(sql, tatekanData.title, tatekanData.image, tatekanData.description, tatekanData.pos_x, tatekanData.pos_y)

    def jsonifyData(title, image, description, pos_x, pos_y):
        
        return jsonify({{"title":title, "image":image, "description":description, "pos_x":pos_x, "pos_y":pos_y}})

    # topページに表示するデータの取得
    def getTopData(db_name):
        sql = "select * from db"
        data = []
        db_cur.execute(sql)
        for row in cur.fetchall():
            x = dict(zip([d[0] for d in cur.description], row))
            results.append(x)
            
        return jsonify(data)