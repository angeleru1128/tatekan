from flask import jsonify
import sqlite3

class TatekanData:
    def __init__(self, title, image, description, pos_x, pos_y):
        self.title = title
        self.image = image
        self.description = description
        self.pos_x = pos_x
        self.pos_y = pos_y

    def createFileName(uploaded_name):
        con = sqlite3.connect('tatekandata.db')
        cur = con.cursor()
        fname = list(cur.execute("select count(*) from tatekan;"))[0]
        return str(fname + "." + (uploaded_name.split("."))[-1])

    def insertToDB(tatekanData):
        con = sqlite3.connect('tatekandata.db')
        cur = con.cursor()
        sql = "insert into tatekan(title, image, description, pos_x, pos_y) values(?, ?, ?, ?, ?);"
        cur.execute(sql, tatekanData.title, tatekanData.image, tatekanData.description, tatekanData.pos_x, tatekanData.pos_y)

    def jsonifyData(title, image, description, pos_x, pos_y):
        return jsonify({{"title":title, "image":image, "description":description, "pos_x":pos_x, "pos_y":pos_y}})

    def getTopData():
        con = sqlite3.connect('tatekandata.db')
        cur = con.cursor()
        sql = "select * from tatekan"
        data = []
        cur.execute(sql)
        for row in cur.fetchall():
            x = dict(zip([d[0] for d in cur.description], row))
            x['pos'] = str(x['pos_x'])  + "," + str(x['pos_y'])  + "," + str(40)
            data.append(x)
        con.close()

        return jsonify(data)