mport unittest 
import requests
import json 
from fractions import Fraction 

n1 = [2,11.2,21/7,4/4,11.75]
n2 = [7,21.7,11/21,7/11,21.1]

subtraction_script = []
subtraction_test = []

for i in range(0,len(n1)):
        parameters={"A":Fraction(n1[i]),"B":Fraction(n2[i])}
        
        test_s = n1[i] - n2[i]
        subtraction_test.append(round(test_s,3))
        
        url_b = 'http://127.0.0.1:5000/sub'
        r2 = requests.get(url_a, params=parameters)
        data2 = r2.json()
        subtraction_script.append(round(data2,3))
        
        
         if subtraction_script[i] == subtraction_test[i]:
                print"subtraction successfull:OK"
        else:
                print"subtraction failed"


