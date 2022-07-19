from flask import Flask


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST','PUT','DELETE'])
def api():
    if request.methd == 'GET':
        pass
    if request.method == 'POST':
        pass
    if request.methd == 'PUT':
        pass
    if request.methd == 'DELETE':
        pass
            