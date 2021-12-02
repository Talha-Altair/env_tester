from flask import *
import os

app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def home():

    data = os.environ

    return jsonify(data)

if __name__ == "__main__":

    app.run(port=8500)
