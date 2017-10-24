import requests

def vaultinit():
    url = 'http://127.0.0.1:8200/v1'
    payload = {'secret_shares': 1, 'secret_threshold': 1}
    initstat = requests.get('{}/sys/init'.format(url))
    #Is Vault already initalized?
    if initstat.json()['initialized'] == True:
        raise Error
    initreq = requests.put('{}/sys/init'.format(url), json=payload)
    unsealreq = requests.put('{}/sys/unseal'.format(url), json={'key': initreq.json()['keys_base64'][0]})
    default_token= requests.post('{}/auth/token/create'.format(url), headers={"X-Vault-Token": initreq.json()['root_token']}, json={"no_default_policy": "true"})
    with open("supersecrets", "w+") as out:
        out.write(default_token.json()['auth']['client_token'])
