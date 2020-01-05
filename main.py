def subtraction():
    value1=request.args.get('A',default = 0, type = Fraction)
    value2=request.args.get('A',default = 0, type = Fraction)
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
