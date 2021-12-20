import requests
from requests import request


def nearest_scoot():
    url = 'https://uram.ddns.net/uram_bot/find'
#номер телефона пользователя, lat - широта lon - долгота
    req = {'phone':'+7999888888',
            'lat':'56.9993738',
           'lon':'54.953738'}
    res = {'result': True, 'data':{}}


    num = input('введите номер телефона: ')
    req['phone'] = num
    req_j = requests.post(url, json=req)
    req_data = req_j.json()
    res_j = requests.post(url, json=res)
    if req_j.status_code == 200:
        print(res_j.url, req_j.url, req_data)
    else:
        print('что-то пошло не так')


test = nearest_scoot()

