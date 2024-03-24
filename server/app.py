#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f'{parameter}'

@app.route('/count/<int:integer>')
def count(integer):
    c = ""
    for num in range(integer):
        c += f'{num}\n'
    return c

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    num = None
    if operation == "+":
        num = num1 + num2
    elif operation == "-":
        num = num1 - num2
    elif operation == "*":
        num = num1 * num2
    elif operation == "div":
        num = num1/num2
    elif operation == "%":
        num = num1 % num2
    else:
        return 'somethign happened bad'
    
    num = str(num)
    return num

    

