from flask import Flask, render_template, request
from fractions import Fraction


app = Flask(__name__)
@app.route('/')
def index():
    return 'Usage;\n<Operation>?A=<Value1>&B=<Value2>\n'


@app.route('/add', methods=['GET','POST'])
def addition():
    value1=request.args.get('A',default = 0, type = Fraction)
    value2=request.args.get('B',default = 0, type = Fraction)
    result=value1+value2
    x=str(result).split('/')
    if len(x) == 2:
        y=float(x[0])/float(x[1])
        z=str(y).split(".")
        if z[1] == '0':
            return " %s\n" %z[0]
        else:
            return " %s\n" %y

    else:
        n=str(result).split(".")
        return " %s \n" % n[0]

@app.route('/sub', methods=['GET','POST'])
def subtraction():
    value1=request.args.get('A',default = 0, type = Fraction)
    value2=request.args.get('B',default = 0, type = Fraction)
    result=value1-value2
    x=str(result).split('/')
    if len(x) == 2:
        y=float(x[0])/float(x[1])
        z=str(y).split(".")
        if z[1] == '0':
            return " %s\n" %z[0]
        else:
            return " %s\n" %y

    else:
        n=str(result).split(".")
        return " %s \n" % n[0]

@app.route('/mul', methods=['GET','POST'])
def multiplication():
    value1=request.args.get('A',default = 0, type = Fraction)
    value2=request.args.get('B',default = 0, type = Fraction)
    result=value1*value2
    x=str(result).split('/')
    if len(x) == 2:
        y=float(x[0])/float(x[1])
        z=str(y).split(".")
        if z[1] == '0':
            return " %s\n" %z[0]
        else:
            return " %s\n" %y

    else:
        n=str(result).split(".")
        return " %s \n" % n[0]

@app.route('/div', methods=['GET','POST'])
def division():
    value1=request.args.get('A',default = 0, type = Fraction)
    value2=request.args.get('B',default = 0, type = Fraction)
    result=value1/value2
    x=str(result).split('/')
    if len(x) == 2:
        y=float(x[0])/float(x[1])
        z=str(y).split(".")
        if z[1] == '0':
            return " %s\n" %z[0]
        else:
            return " %s\n" %y

    else:
        n=str(result).split(".")
        return " %s \n" % n[0]

if __name__ == '__main__':
    app.run(debug=True)


