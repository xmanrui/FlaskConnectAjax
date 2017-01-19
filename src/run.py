from flask import Flask, render_template, request
from flask import jsonify

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
    d = {'name': 'xmr', 'age': 18}
    return jsonify(d)

@app.route('/mylist')
def mylist():
    l = ['xmr', 18]
    return jsonify(l)




if __name__ == '__main__':
    app.run()
