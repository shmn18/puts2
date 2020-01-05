import unittest 
import requests
import json 
from fractions import Fraction 

n1 = [2,11.2,21/7,4/4,11.75]
n2 = [7,21.7,11/21,7/11,21.1]

addition_script = []
addition_test = []
subtraction_script = []
subtraction_test = []
multiplication_script = []
multiplication_test = []
division_script = []
division_test= []

for i in range(0,len(n1)):
        parameters={"A":Fraction(n1[i]),"B":Fraction(n2[i])}

        test_a = n1[i] + n2[i]
        addition_test.append(round(test_a,3))

        test_s = n1[i] - n2[i]
        subtraction_test.append(round(test_s,3))

        test_m = n1[i] * n2[i]
        multiplication_test.append(round(test_m,3))

        test_d = n1[i] / n2[i]
        division_test.append(round(test_d,3))

        url_a = 'http://127.0.0.1:5000/add'
        r1 = requests.get(url_a, params=parameters)
        data1 = r1.json()
        addition_script.append(round(data1,3))

        url_b = 'http://127.0.0.1:5000/sub'
        r2 = requests.get(url_a, params=parameters)
        data2 = r2.json()
        subtraction_script.append(round(data2,3))

        url_m = 'http://127.0.0.1:5000/mul'
        r3 = requests.get(url_a, params=parameters)
        data3 = r3.json()
        multiplication_script.append(round(data3,3))

        url_d = 'http://127.0.0.1:5000/div'
        r4 = requests.get(url_a, params=parameters)
        data4 = r4.json()
        division_script.append(round(data4,3))

        if addition_script[i] == addition_test[i]:
                print"addition successfull:OK"
        else:
                print"addition failed"
        
        if subtraction_script[i] == subtraction_test[i]:
                print"subtraction successfull:OK"
        else:
                print"subtraction failed"

        if multiplication_script[i] == multiplication_test[i]:
                print"multiplication successfull:OK"
        else:
                print"multiplication failed"

        if division_script[i] == division_test[i]:
                print"division successfull:OK"
        else:
                print"division failed"
