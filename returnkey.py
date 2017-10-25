#!/usr/local/bin/python3
import vaultinit
import pyvault
from bottle import route, run, template

vaultinit.vaultinit()
pyvault.pyvault()

@route('/pyvault')
def index():
    return pyvault.pyvault()

run(host='localhost', port=8080)
