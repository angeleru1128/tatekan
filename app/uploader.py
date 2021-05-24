from flask import Flask, render_template,jsonify
from flask_cors import CORS
import sqlite3

# 画像ファイルのファイル名を生成
# 
def createFileName(db):
    fname = db
    return fname

# データベースに登録
def insertToDB():
