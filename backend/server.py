from flask import Flask
from project import dataebay, dataamz , mergearray

# contact between endpoints 
app = Flask(__name__)

@app.route("/members")

def arraypush(): 
   return{"array": mergearray(dataamz,dataebay)}

if __name__ == "__main__": 
    app.run(debug=True)
