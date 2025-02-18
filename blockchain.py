import hashlib
import time


# Define a class for a Block
class Block:
    def __init__(self, block_id, previous_block_hash, timestamp, content):
        self.block_id = block_id
        self.previous_block_hash = previous_block_hash
        self.timestamp = timestamp
        self.content = content
        self.block_hash = self.compute_block_hash()

    def compute_block_hash(self):
        block_data = f"{self.block_id}{self.previous_block_hash}{self.timestamp}{self.content}"
        return hashlib.sha256(block_data.encode('utf-8')).hexdigest()


# Function to create the genesis block (first block)
def create_genesis_block():
    return Block(0, "0", int(time.time()), "Genesis Block")


# Function to create a new block based on the last block in the chain
def create_new_block(last_block, content):
    block_id = last_block.block_id + 1
    timestamp = int(time.time())
    return Block(block_id, last_block.block_hash, timestamp, content)


# Function to validate the entire blockchain
def validate_chain(blockchain):
    for i in range(1, len(blockchain)):
        if blockchain[i].block_hash != blockchain[i].compute_block_hash():
            return False
        if blockchain[i].previous_block_hash != blockchain[i - 1].block_hash:
            return False
    return True


# Proof of Work (mining) function
def mine_block(block, difficulty):
    prefix = '0' * difficulty
    while not block.block_hash.startswith(prefix):
        block.timestamp += 1
        block.block_hash = block.compute_block_hash()
    return block
