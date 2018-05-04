from flask import Flask, render_template
import json
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def hello_world():
    res = []
    try:
        with open("../test.json", 'r') as f:
            res = json.load(f)
    except FileNotFoundError:
        res = { "error": "File Not Found" }
    except json.decoder.JSONDecodeError:
        res = "This is not a json"
    return render_template('index.html', movie_list=res)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
