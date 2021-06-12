#from flask.wrappers import Request
from flask.helpers import url_for
from flask.json import jsonify
from flask.wrappers import Response
from werkzeug.datastructures import Headers
from werkzeug.wrappers import response
import TatekanData as TD
from flask import Flask, request, abort
from flask_cors import CORS
import os

UP_DIR = "./static/tatekan_images"

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024*4 * 1024*4
app.config["JSON_AS_ASCII"] = False
cors = CORS(app, resources={r"/*": {"origins": "*"}}, headers='Content-Type')
app.config['UPLOAD_FOLDER'] = UP_DIR
app.config["CORS_HEADERS"] = 'Content-Type'

# allowed extensions
ALLOWED_EXTENSIONS = ["jpg", "png", "jpeg", "gif"]
def allowed_file(fname):
  return '.' in fname and fname.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# upload tatekan
@app.route("/upload", methods=["POST"])
def upload():
  
  if request.method == None:
    return abort(Response("method is None"))
  if 'upLoadFile' not in request.files:
    return abort(Response("file is None"))
  
  file = request.files["uploadFile"]
  filename = TD.createFileName(str(file.filename))
  file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
  
  if filename == '':
    return abort(Response("filename is None"))
  if not allowed_file(filename):
    return abort(Response("the type of file is not allowed"))
  

  """
  tk = TD.TatekanData(
    title = "sample_title", #request.json["title"],
    image = "sample_name",#TD.TatekanData.createFileName(str(file.filename)),
    description ="sample_description", #request.json["description"],
    pos_x = 10,#request.json["pos_x"],
    pos_y = 12#request.json["pos_y"]
  )
  """
  if False == TD.insertToDB(request.form["title"], filename, request.form["description"], request.form["pos_x"], request.form["pos_y"]):
    return abort(Response("Failed to insert to db"))
  #TD.TatekanData.insertToDB(tk)

  return url_for(request.url)
"""
@app.errorhandler(400)
@app.errorhandler(500)
@app.errorhandler(404)
def error_handler(error):
  res = jsonify({'message': error.name, 'result': error.code})
  return res, error.code
"""
# show top page
@app.route("/topdata", methods=["GET"])
def top_page():  
  return TD.getTopData()

if __name__ == '__main__':                        
    app.run(host="0.0.0.0", port=5000, debug=False)