from flask import Flask
from flask import jsonify, request, abort

app = Flask(__name__)

names = ["Habib", "Okanla"]


@app.route('/')
def hello_world():
    return 'Hello World Jason!!'


@app.route('/get_names', methods=['GET'])
def get_tasks():
    return jsonify({'names': names})


# #Add 2 numbers passed as json.
@app.route('/add', methods=['POST'])
def add_nums():
    if not request.json or not 'num1' in request.json or not 'num2' in request.json:
        abort(400)
    return jsonify({'result': request.json['num1'] + request.json['num2']}), 201


if __name__ == '__main__':
    app.run()
