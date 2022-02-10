from flask import *
import os
import time

app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def home():

    data = dict(os.environ)

    return jsonify(data)

if __name__ == "__main__":

    app.run(port=8500, host="0.0.0.0", debug=True)
