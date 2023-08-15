from flask import Flask
from flask import Flask, jsonify,request
app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    response = {"code":200,"content":"hello world!"}
    return jsonify(response),200
    # return 'Hello world!', 200

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.get_json()
    first_number = data["first"]
    second_number = data["second"]
    result = first_number + second_number

    response = {
        "Status code": 200,
        "result": result
    }
    return jsonify(response), 200

@app.route("/calculator/add/<int:first>/<int:second>", methods=['GET'])
def perform_addition(first, second):
    result = first + second

    response = {
        "result": result
    }
    return jsonify(response), 200

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data=request.get_json()
    firstnum=data["first"]
    secondnum=data["second"]
    result=firstnum-secondnum
    res={
        "Status code": 200,
        "result": result 
    }
    return jsonify(res),200

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
