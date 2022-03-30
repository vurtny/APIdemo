import requests

# 请求的url地址
url1 = "http://172.16.2.166/api/students?name=%E8%A2%81%E6%98%A5%E7%87%95&type=0&teacherChildrenType=0&livingInSchool=0&noGuardianType=0&isSpecialRegion=0"
# 请求头
headers = {"content-type": "application/json", "token": "73890bf0c70ed1707dddb0218a97970f"}
respon = requests.get(url1, headers=headers)
print(respon.json()) #获取所有的返回结果
kk = respon.json()['result'][0]["name"]#只获取返回的skuName值
print(kk)
#第一个接口返回的skuName数据 作为第二个接口userName的入参
url2 = "http://172.16.2.166/api/guardians"

data = {"studentName": kk}
result = requests.get(url2, params=data, headers=headers)
print(result.json())
# url3 = result.url
# print(url3)
# sk = requests.get(url3, headers=headers)
# print(sk.json())