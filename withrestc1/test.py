import requests
import json
import time
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'
# print('get request')
# def get_resources(id=None):
#     data={}
#     if id is not None:
#         data={
#         'id':id
#         }
#     resp= requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())
# get_resources()
# time.sleep(5)
# print('Create record')
# def create_resource():
#     new_emp={
#     'eno':500,
#     'ename':'Sai',
#     'esal':8000,
#     'eaddr':'Phopnar',
#     }
#     r=requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
#     print(r.status_code)
#     print(r.json())
# create_resource()
# time.sleep(10)
# print('update record')
def update_resource(id):
    new_data={
    'id':id,
    'ename':'Sharukh',
    'esal':9001,
    }
    r=requests.put(BASE_URL+ENDPOINT,data=json.dumps(new_data))
    print(r.status_code)
    print(r.json())
update_resource(6)
# time.sleep(10)
# print('delete Operation')
# def delete_resource(id):
#     data={
#     'id':id,
#     }
#     r=requests.delete(BASE_URL+ENDPOINT,data=json.dumps(data))
#     print(r.status_code)
#     print(r.json())
# delete_resource(1)
