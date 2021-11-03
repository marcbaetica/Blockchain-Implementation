import json
from hashlib import sha256
from time import time


class Block:
    def __init__(self, previous_hash, transactions, proof_of_work):
        self.timestamp = time()
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.proof_of_work = proof_of_work
        self.hash = self.generate_block_hash()
        # Index necessary?

    def generate_block_hash(self):
        block_data = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_data.encode()).hexdigest()
