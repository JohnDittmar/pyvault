#!/usr/local/bin/python3
import requests


def pyvault():
    url = 'http://127.0.0.1:8200/v1'
    content_type = {'Content-Type': 'application/json'}
    with open('supersecrets') as secrets:
        client_token={"X-Vault-Token": secrets.read()}
    make_a_kv = requests.post('{}/secret/foo'.format(url), headers=client_token, json={"value":"bar"} )
    return_value = requests.get('{}/secret/foo'.format(url), headers=client_token)
    value = (return_value.json()['data']['value'])
    return value 


if __name__ == '__main__':
    pyvault()
