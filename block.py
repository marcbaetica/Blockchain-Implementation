from hashlib import sha256
from pprintpp import pprint


class Block:
    def __init__(self, transactions, block=None):
        if block is None:
            self.number = 1
            self.transactions = transactions
            self.previous_hash = 0
            self.current_hash = self.calculate_hash()
        else:
            self.number = block.number + 1
            self.transactions = transactions
            self.previous_hash = block.current_hash
            self.current_hash = self.calculate_hash()

    def __repr__(self):
        return str([self.previous_hash, self.transactions])

    def calculate_hash(self):
        block_data = repr(self)
        block_data = block_data.encode()  # Is representation enough?
        return sha256(block_data).hexdigest()
