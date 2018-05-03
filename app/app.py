from flask import Flask, render_template, request, redirect, jsonify
import json
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def hello_world():
   return render_template('index.html')

@app.route('/data', methods=['POST'])
def handle_data():
    a1 = str(request.form['a1'])
    a2 = str(request.form['a2'])
    with open('../actors.json', "w") as f:
        a_dict = { "actor1": a1, "actor2": a2 }
        json.dump(a_dict, f)
    return redirect('/result')

@app.route('/result')
def display_result():
    res = []
    try:
        with open("../result.json", 'r') as f:
            res = json.load(f)
    except FileNotFoundError:
        res = { "error": "File Not Found" }
    except json.decoder.JSONDecodeError:
        res = "This is not a json"
    return render_template('results.html', movie_list=res

if __name__ == '__main__':
    app.run(host='0.0.0.0')
