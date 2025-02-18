from blockchain import Block, create_genesis_block, create_new_block, validate_chain, mine_block

# Creating the blockchain with the genesis block
genesis_block = create_genesis_block()
block_1 = create_new_block(genesis_block, "Block 1 content")
block_2 = create_new_block(block_1, "Block 2 content")

# Create the blockchain list
blockchain = [genesis_block, block_1, block_2]

# Validate the blockchain
print(f"Is the blockchain valid? {validate_chain(blockchain)}")

# Display block hashes
print(f"Genesis Block Hash: {genesis_block.block_hash}")
print(f"Block 1 Hash: {block_1.block_hash}")
print(f"Block 2 Hash: {block_2.block_hash}")

# Perform mining on Block 2 with a difficulty of 4
difficulty = 4
mined_block = mine_block(block_2, difficulty)

# Show the mined block's hash
print(f"Mined Block Hash: {mined_block.block_hash}")
