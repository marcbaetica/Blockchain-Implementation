from BC.blockchain import Blockchain
from BC.block import Block
from json import JSONEncoder


# For JSON parsing when serving contents via HTTP.
class BlockchainEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Blockchain) or isinstance(obj, Block):
            return obj.__dict__
        JSONEncoder.default(self, obj)  # Letting the base class default method raise the TypeError
