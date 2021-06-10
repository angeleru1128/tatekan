#from flask.wrappers import Request
from flask.helpers import url_for
from flask.json import jsonify
from flask.wrappers import Response
from werkzeug.datastructures import Headers
from werkzeug.wrappers import response
import TatekanData as TD
from flask import Flask, request, abort
from flask_cors import CORS

UP_DIR = "../static/tatekan_images"

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
cors = CORS(app, resources={r"/*": {"origins": "*"}}) #, headers='Content-Type')
app.config['UPLOAD_FOLDER'] = UP_DIR
#app.config["CORS_HEADERS"] = 'Content-Type'

# allowed extensions
ALLOWED_EXTENSIONS = ["jpg", "png", "jpeg", "gif"]
def allowed_file(fname):
  return '.' in fname and fname.resplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# upload tatekan
@app.route("/upload", methods=["POST"])
def upload():
  '''
  if request.method == None:
    return abort(Response("method is None"))
  if request.files == None:
    return abort(Response("file is None"))
  file = request.files["file"]
  if file.filename == "":
    return abort(Response("filename is None"))
  if not allowed_file(file.filename):
    return abort(Response("the type of file is not allowed"))
  '''
  tk = TD.TatekanData(
    title = request.json["title"],
    image = TD.TatekanData.createFileName(request.json["image"]),
    description = request.json["description"],
    pos_x = request.json["pos_x"],
    pos_y = request.json["pos_y"]
  )

  TD.TatekanData.insertToDB(tk)

  return url_for(request.url)

@app.errorhandler(400)
@app.errorhandler(500)
@app.errorhandler(404)
def error_handler(error):
  res = jsonify({'message': error.name, 'result': error.code})
  return res, error.code

# show top page
@app.route("/topdata", methods=["GET"])
def top_page():  
  return TD.TatekanData.getTopData()

if __name__ == '__main__':                        
    app.run(host="0.0.0.0", port=3000)