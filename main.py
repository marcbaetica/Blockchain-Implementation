import json
from BC.blockchain import Blockchain
from BC.encoders import BlockchainEncoder
from flask import Response
from flask.app import Flask
from pprintpp import pprint
from utils.utils import generate_random_transactions


webserver = Flask('Blockchain_Interface')

chain = Blockchain()
pprint(chain.__dict__, width=1)
pprint(chain.last_block.__dict__)

for _ in range(5):
    chain.add_new_transactions(generate_random_transactions())

pprint(chain.__dict__)

chain.mine()

print(f'Chain integrity is: {chain.verify_chain_integrity()}\n')

# Compromising the chain by breaking its integrity at block 5:
chain.blocks[5].previous_hash = 'aaa'
print(f'Chain integrity is: {chain.verify_chain_integrity()}')


@webserver.get('/chain')
def blockchain_structure():
    return Response(json.dumps(chain, cls=BlockchainEncoder), mimetype='application/json')


webserver.run()
