from flask import Flask, request, jsonify
from project import dataebay, dataamz , mergearray
from flask_cors import CORS

# contact between endpoints 
app = Flask(__name__)
cors = CORS(app)

@app.route("/")

def arraypush(): 
   return{"array": mergearray(dataamz,dataebay)}

@app.route("/receiver", methods=["POST"])
def postME():
 data = request.get_json()
 data = jsonify(data)
 return data

if __name__ == "__main__": 
    app.run(debug=True)
