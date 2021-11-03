from BC.blockchain import Blockchain
from pprintpp import pprint


chain = Blockchain()
pprint(chain.__dict__, width=1)
pprint(chain.last_block.__dict__)
