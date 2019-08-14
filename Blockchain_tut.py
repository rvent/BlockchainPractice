import datetime
import hashlib
import json
import numpy as np

class Block(object):

    def __init__(self, fro, to, amount):
        self._index = 0
        self.transaction = {
            "block#" : self._index,
            "block_creation_time" : str(datetime.datetime.now()),
            "from" : fro,
            "to" : to,
            "amount" : amount,
            "timestamp" : str(datetime.datetime.now())
            }
        self._previous_hash = "None"
        self._current_hash = self.calculateHash()
        
    @property
    def previous_hash(self):
        return self._previous_hash

    @previous_hash.setter
    def previous_hash(self, new_hash):
        self._previous_hash = new_hash

    @property
    def current_hash(self):
        return self._current_hash

    @current_hash.setter
    def current_hash(self, new_hash):
        self._current_hash = new_hash

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, inc):
        self._index = inc
        
    def __str__(self):
        return """ block= {
        transaction : %s
        previous_hash: %s
        hash: %s
        }"""%(self.transaction, self.previous_hash, self.current_hash)

    def __repr__(self):
        return str(self.transaction)

    def calculateHash(self):
        trans =  json.dumps(self.transaction)
        return hashlib.sha256((str(self.index) + self.previous_hash + trans).encode()).hexdigest()
    

class Blockchain(object):

    def __init__(self, genesis_block=None):
        if genesis_block == None:
             self.chain = [self.createGenesisBlock()]
        else:
            self.chain = [genesis_block]

    def createGenesisBlock(self):
        return Block("None", "None", 0)

    def addBlock(self, new_block):
        old_block = self.getLatestBlock()
        new_block.previous_hash = old_block.current_hash
        new_block.index = (old_block.index + 1)
        new_block.transaction["block#"] = new_block.index
        new_block.transaction["timestamp"] = str(datetime.datetime.now())
        self.chain.append(new_block)

    def getLatestBlock(self):
        return self.chain[-1]

        
        
