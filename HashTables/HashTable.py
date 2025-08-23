import math

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    def __init__(self, size=11, threshold=0.7):
        self.size = self._next_prime(size)
        self.threshold = threshold
        self.table = [None] * self.size # slots hold: None | Node
        self.count = 0

    # --- Hash & load factor ---
    def _hash(self, key):
        return hash(key) % self.size
    
    def load_factor(self):
        return self.count / self.size

    # --- Core operations (linear probing) ---
    def insert(self, key, value):
        # Rehash BEFORE insertion if the next insert would exceed the threshold
        self.count += 1
        if self.load_factor() > self.threshold:
            self._rehash(self._next_prime(self.size))
        idx = self._hash(key)
        probes = 0
        while probes < self.size:
            slot = self.table[idx]
            if slot is None:
                self.table[idx] = Node(key, value)
                return
            idx = (idx + 1) % self.size
            probes += 1 
    
    def search(self, key):
        idx = self._hash(key)
        probes = 0
        while probes < self.size:
            slot = self.table[idx]
            if slot is None:
                return None # key not present
            if slot.key == key:
                return slot.value
            idx = (idx + 1) % self.size
            probes += 1
        return None

    def delete(self, key):
        idx = self._hash(key)
        probes = 0
        while probes < self.size:
            slot = self.table[idx]
            if slot is None:
                return False
            if slot.key == key:
                self.table[idx] = None
                self.count -= 1
                return True
            idx = (idx + 1) % self.size
            probes += 1
        return False

    def _rehash(self, new_size):
        old_table = self.table
        self.size = new_size
        self.table = [None] * self.size
        old_count = self.count
        self.count = 0
        for slot in old_table:
            if slot is not None:
                self.insert(slot.key, slot.value)
            
    def _is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n%i == 0:
                return False
        return True
    
    def _next_prime(self, n):
        new_size = n * 2
        while not self._is_prime(new_size):
            new_size += 1
        return new_size


# Example: size=7, threshold=0.7; will rehash to first prime > 14 when needed

ht = HashTable(size=7, threshold=0.7)
for k, v in [(50, 'A'), (700, 'B'), (76, 'C'), (85, 'D'), (92, 'E')]:
    ht.insert(k, v)
print('92 ->', ht.search(92))
ht.delete(76)
print('76 ->', ht.search(76))        