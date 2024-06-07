import requests
import json
import os

# url = https://jsonplaceholder.typicode.com/todos/

n = int() 

if n > 0 or n <=100 :
    input("Ingrese un nuemro entre los valores 0 y 100:")

else:
    input("Debe ser exclusivamente un nuemro entre los valores 0 y 100:")

    
repose = requests.get ("https://jsonplaceholder.typicode.com/todos/{n}")
post = repose.json

print(post)
# def primos () :
#     if post 'id' == n % 2 == 0 or n % 3 == 0 :
