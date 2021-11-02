from block import Block
from utils import print_block_details


block = Block(['X gives Y $100', 'Y gives Z $20'])
print_block_details(block)
block = Block(['Z gives X $20'], block)
print_block_details(block)
block = Block(['Y gives Z $37'], block)
print_block_details(block)
block = Block(['Y gives X $200', 'X gives Z $423'], block)
print_block_details(block)
block = Block(['X gives Z $52'], block)
print_block_details(block)

# TODO: link and iterate through data struct.
