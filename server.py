from flask import Flask, escape, request
from drivers import drivers, get_driver

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def create():
    data = request.get_json()
    did = data['id']
    driver, id = get_driver(did)
    if driver == None or id == None:
        return '', 404
    tx_id = driver.create(request.get_json())
    return {'result': did}

@app.route('/<did>', methods = ['GET'])
def index(did):
    driver, id = get_driver(did)
    if driver == None or id == None:
        return '', 404
    resolved = driver.resolve(did)
    if resolved == None:
        return '', 404
    return resolved
