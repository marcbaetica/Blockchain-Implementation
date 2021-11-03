from BC.block import Block


class Blockchain:
    def __init__(self):
        self.pending_transactions = []
        self.blocks = []
        self.create_genesis_block()

    def create_genesis_block(self):
        return self.blocks.append(Block(0, [], 0))  # TODO: proof of work should be larger

    @property
    def last_block(self):
        return self.blocks[-1]

    def create_new_block(self):
        pass

    def verify_chain_integrity(self):
        pass

    def process_new_transactions(self):  # Mining if pending transactions exist?
        pass
