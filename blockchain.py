import hashlib
import time

class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        content = str(self.timestamp) + self.data + self.previous_hash
        return hashlib.sha256(content.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block("Genesis Block", "0")

    def add_block(self, data):
        previous = self.chain[-1]
        new_block = Block(data, previous.hash)
        self.chain.append(new_block)

bc = Blockchain()
bc.add_block("Rohit sends 10 coins")
bc.add_block("Amit sends 5 coins")

for block in bc.chain:
    print(block.data, block.hash)
  
