import requests

url = 'http://172.16.2.166/api/login'
data = {"loginName": "admin",
        "password": "admin123",
        "remember": True}
# post请求
result = requests.post(url=url, json=data)
# get请求
# result = requests.get(url=url, params=data)
# 三种响应方式
print(result.content)
print(result.json())
print(result.text)