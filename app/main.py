#from flask.wrappers import Request
from flask.helpers import url_for
from TatekanData import TatekanData
from flask import Flask, render_template,jsonify,request, abort
from flask_cors import CORS
import sqlite3

UP_DIR = "../asserts"

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
cors = CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:3000"}})
app.config['UPLOAD_FOLDER'] = UP_DIR

# allowed extensions
ALLOWED_EXTENSIONS = [".jpg", ".png", "jpeg", "gif"]
def allowed_file(fname):
  return '.' in fname and fname.resplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# upload tatekan
@app.route("/upload", methods=["POST"])
def upload():
  if request.method == None:
    return abort(400)
  if request.files == None:
    return abort(400)
  file = request.files["file"]
  if file.filename == "":
    return abort(400)
  if not allowed_file(file.filename):
    return abort(400)
  
  con = sqlite3.connect("tatekandata.db")
  cur = con.cursor()

  tk = TatekanData(
    title = request.json["title"],
    image = TatekanData.createFileName(cur, request.json["image"]),
    description = request.json["description"],
    pos_x = request.json["pos_x"],
    pos_y = request.json["pos_y"]
  )

  TatekanData.insertToDB(cur, tk)

  return url_for(request.url)

# show top page
@app.route("/")
def top_page():
  con = sqlite3.connect("tatekandata.db")
  cur = con.cursor()
  tks = list(cur.execute("select * from tatekan;"))
  
  return jsonify(tks)

if __name__ == '__main__':                        
    app.run(host="0.0.0.0", port=80, debug=True)