import unittest 
import requests
import json 
from fractions import Fraction 

n1 = [2,11.2,21/7,4/4,11.75]
n2 = [7,21.7,11/21,7/11,21.1]

addition_script = []
addition_test = []

for i in range(0,len(n1)):
        parameters={"A":Fraction(n1[i]),"B":Fraction(n2[i])}
        
        test_a = n1[i] + n2[i]
        addition_test.append(round(test_a,3))
        
        url_a = 'http://127.0.0.1:5000/add'
        r1 = requests.get(url_a, params=parameters)
        data1 = r1.json()
        addition_script.append(round(data1,3))
        
        if addition_script[i] == addition_test[i]:
                print"addition successfull:OK"
        else:
                print"addition failed"
