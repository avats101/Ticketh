import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

        self.new_block(previous_hash="Lorem Ipsum", proof=1)

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.pending_transactions = []
        self.chain.append(block)

        return block

    @property
    def last_block(self):
 
        return self.chain[-1]


    def new_transaction(self, sender, recipient, amount,num,eventid,start,sale):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
            'nooftickets':num,
            'eventid':eventid,
            'StartingTicketID':start,
            'first_sale':sale
        }
        self.pending_transactions.append(transaction)
        return self.last_block['index'] + 1

    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash


blockchain = Blockchain()
t1 = blockchain.new_transaction("Praneel","Organiser1",0.1,10,"S0001","T01",True)
t2 = blockchain.new_transaction("Aryan", "Organiser2",0.2,10,"S0001","T11",True)
t3 = blockchain.new_transaction("Iownit", "Organiser3",0.3,10,"S0001","T21",True)
blockchain.new_block(2)

t4 = blockchain.new_transaction("Tim","Iownit",0.12,3,"S0001","T21",False)
t5 = blockchain.new_transaction("Tim","Aryan",0.15,5,"S0001","T11",False)
t6 = blockchain.new_transaction("Tim","Aryan",0.2,5,"S0001","T16",False)
t7 = blockchain.new_transaction("Tim","Praneel",0.2,10,"S0001","T01",False)
blockchain.new_block(3)

print("Genesis block: ", blockchain.chain)