def print_block_details(block):
    print(f'Block number {block.number} has:')
    print(f'    -> Previous hash: {block.previous_hash}')
    print(f'    -> Transactions hash: {block.transactions}')
    print(f'    -> Current hash: {block.current_hash}\n')
