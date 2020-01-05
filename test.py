import unittest 
import requests
import json 
from fractions import Fraction 

n1 = [2,21,5,8]
n2 = [7,11,3,4]

multiplication_script = []
multiplication_test = []

for i in range(0,len(n1)):
        parameters={"A":Fraction(n1[i]),"B":Fraction(n2[i])}
        
        test_m = n1[i] * n2[i]
        multiplication_test.append(round(test_m,3))
        
        url_m = 'http://127.0.0.1:5000/mul'
        r3 = requests.get(url_m, params=parameters)
        data3 = r3.json()
        multiplication_script.append(round(data3,3))
        
        if multiplication_script[i] == multiplication_test[i]:
                print"multiplication successfull:OK"
        else:
                print"multiplication failed"
