from BC.block import Block


class Blockchain:
    def __init__(self):
        self.pending_transactions = []
        self.blocks = []
        self.create_genesis_block()

    def create_genesis_block(self):
        return self.blocks.append(Block(0, 0, [], 0))  # TODO: proof of work should be larger

    @property
    def last_block(self):
        return self.blocks[-1]

    def create_new_block(self, transaction):
        last_block = self.blocks[-1]
        self.blocks.append(Block(last_block.index + 1, last_block.hash, transaction, last_block.proof_of_work))

    def verify_chain_integrity(self):
        """Verifies the chain integrity by validating that the hash value of a block is the same as the previous_hash
        value of the next block. The integrity of the chain confirms the chain's immutability from malicious hacking.

        :return: Bool value representing the hash value.
        """
        hashes_from_blocks = [(block.previous_hash, block.hash) for block in self.blocks]
        for i in range(len(hashes_from_blocks)-1):
            if hashes_from_blocks[i][1] != hashes_from_blocks[i+1][0]:
                print(f'Hash [{hashes_from_blocks[i][1]}] from block [{i}] does not match the'
                      f' previous hash property [{hashes_from_blocks[i+1][0]}] of block [{i+1}].'
                      f' Chain is now broken starting with block [{i+1}]')
                return False
        return True

    def add_new_transactions(self, transactions):
        """Add transactions pending processing in future blocks.

        :param transactions: Transaction(s) that need processing. Can be a sting or list of strings.
        :return: None
        """
        if isinstance(transactions, list):
            [self.pending_transactions.append(transaction) for transaction in transactions]
            return
        if isinstance(transactions, str):
            self.pending_transactions.append(transactions)
            return
        raise TypeError(f'New transactions object must be of type string or list of strings.')

    def process_new_transaction(self, transaction):
        self.create_new_block(transaction)
        self.pending_transactions.remove(transaction)

    def mine(self):
        if not self.pending_transactions:
            print('No transactions pending at the moment.')
        # TODO: Add Proof of Work here for increased computational complexity.
        # .copy() because we remove items from the original list during iteration (read loop functionality)
        for transaction in self.pending_transactions.copy():
            self.process_new_transaction(transaction)
