from flask import Flask, render_template, request
from flask import jsonify
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = "dfdfdffdad"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mystring')
def mystring():
    return 'my string'


@app.route('/dataFromAjax')
def dataFromAjax():
    test = request.args.get('mydata')
    print(test)
    return 'dataFromAjax'


@app.route('/mydict', methods=['GET', 'POST'])
def mydict():
    print('post')
    if request.method == 'POST':
        a = request.form['mydata']
        print(a)
    d = {'name': 'xmr', 'age': 18}
    return jsonify(d)


@app.route('/name', methods=['POST'])
def getname():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    d = {'name': firstname + ' ' + lastname, 'age': 18}
    print(d)
    return jsonify(d)


@app.route('/myform', methods=['POST'])
def myform():
    print('post')
    a = request.form['FirstName']
    print(a)
    d = {'name': 'xmr', 'age': 18}
    return jsonify(d)


@app.route('/mylist')
def mylist():
    l = ['xmr', 18]
    print('mylist')
    return json.dumps(l)  # 用jsonify前端会出错


if __name__ == '__main__':
    app.run()
