from flask import Flask, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# =================================================================== #
# 處理jsonify datetime formate
from flask.json import JSONEncoder
from datetime import date
class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        try:
            if isinstance(obj, date):
                return obj.isoformat()
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)
app.json_encoder = CustomJSONEncoder
# =================================================================== # 

app.config['DEBUG'] = True
app.config['JSON_AS_ASCII'] = False

@app.route("/api/")
def index():
    # return "Hello world"
    return render_template('index.html')

def return_template(code):
    return render_template('pageNotFound.html')


if __name__ == "__main__":
    # use 0.0.0.0 to use it in container
    app.run(host='0.0.0.0')