# requests 에서 json 처리
import requests

# url = "https://jsonplaceholder.typicode.com/todos/1"

# res = requests.get(url)
# print(res.text)
# print(res.content) # binary

# print(res.json()) # json ==> dixt
# print(res.json().keys())
# print(res.json().values())


# json 데이터 여러개 일 때
url = "https://jsonplaceholder.typicode.com/users"

res = requests.get(url)
# print(res.text)

for row in res.json():
    for k, v in row.items():
        print("key : {}, value : {}".format(k, v))
    print()
