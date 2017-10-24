#!/usr/local/bin/python3
import requests

def pyvault():
    url = 'http://127.0.0.1:8200/v1'
    with open('supersecrets', 'r') as secrets:
        client_token=secrets.read()
        return_value = requests.get('{}/secret/foo'.format(url), headers={"X-Vault-Token": client_token})
        return return_value.json()['data']['value']


if __name__ == '__main__':
    pyvault()



curl \
    -H "X-Vault-Token: 5c6f955e-6c2c-b3d7-37eb-6e19ca38b028" \
    -X GET \
    http://127.0.0.1:8200/v1/secret/foo


    curl \
    -H "X-Vault-Token: 5c6f955e-6c2c-b3d7-37eb-6e19ca38b028" \
    -H "Content-Type: application/json" \
    -X POST \
    -d '{"value":"bar"}' \
    http://127.0.0.1:8200/v1/secret/foo
