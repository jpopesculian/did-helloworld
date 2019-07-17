from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair
from pymongo import MongoClient

class BdbDriver:
    def __init__(self):
        self.bdb = BigchainDB('http://localhost:9984')
        self.key_pair = generate_keypair()
        self.mongo = MongoClient('localhost', 27017).bigchain
        self.nonce = 0

    def create(self, data):
        self.nonce = self.nonce + 1
        tx = self.bdb.transactions.prepare(
            operation="CREATE",
            signers=self.key_pair.public_key,
            asset={'data': data})
        signed_tx = self.bdb.transactions.fulfill(
            tx,
            private_keys=self.key_pair.private_key)
        committed = self.bdb.transactions.send_commit(signed_tx)
        return committed['id']

    def resolve(self, did):
        asset = self.mongo.assets.find_one({'data.id': did})
        if asset == None:
            return None
        return asset['data']
