import requests


# response = requests.get(url='http://127.0.0.1:8082/index')

json={
    "name":'wowo',
    "age":"23"
}


response = requests.post(url='http://127.0.0.1:8082/test_10',json=json)
x=response.json()
print(x)
print(type(x))
