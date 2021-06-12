from flask import jsonify
import sqlite3

def createFileName(uploaded_name):
    con = sqlite3.connect('tatekandata.db')
    cur = con.cursor()
    fname = list(cur.execute("select count(*) from tatekan"))[0]
    con.close()
    return str(fname + "." + (uploaded_name.split("."))[-1])

def insertToDB(title, image, description, pos_x, pos_y):
    con = sqlite3.connect('tatekandata.db')
    cur = con.cursor()
    sql = "insert into tatekan(title, image, descriprition, pos_x, pos_y) values(?, ?, ?, ?, ?)"
    try:
        cur.execute(sql, (title, image, description, pos_x, pos_y))
    except:
        return False
    
    con.commit()
    con.close()

def jsonifyData(title, image, description, pos_x, pos_y):
    return jsonify({{"title":title, "image":image, "descriprition":description, "pos_x":pos_x, "pos_y":pos_y}})

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