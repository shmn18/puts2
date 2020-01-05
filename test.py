import unittest 
import requests
import json 
from fractions import Fraction 

n1 = [2,11.2,21/7,4/4,11.75]
n2 = [7,21.7,11/21,7/11,21.1]

division_script = []
division_test= []

for i in range(0,len(n1)):
        parameters={"A":Fraction(n1[i]),"B":Fraction(n2[i])}

        test_d = n1[i] / n2[i]
        division_test.append(round(test_d,3))
        
        url_d = 'http://127.0.0.1:5000/div'
        r4 = requests.get(url_a, params=parameters)
        data4 = r4.json()
        division_script.append(round(data4,3))
        
        if division_script[i] == division_test[i]:
                print"division successfull:OK"
        else:
                print"division failed"
        
        
