class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self, size=11, threshold=0.7):
        self.size = self._next_prime(size)
        self.threshold = threshold
        self.table = [None] * self.size
        self.count = 0

    # Hash & load factor
    def _hash(self, key):
        return hash(key) % self.size

    def load_factor(self):
        return self.count / self.size

    # Insert with quadratic probing
    def insert(self, key, value):
        if self.load_factor() > self.threshold:  # rehash before insert
            self._rehash(self._next_prime(self.size * 2))

        idx = self._hash(key)
        i = 1
        while True:
            slot = self.table[idx]
            if slot is None or slot == "DELETED": # empty or deleted slot 
                self.table[idx] = Node(key, value)
                self.count += 1
                return
            elif slot.key == key:   # update existing key
                slot.value = value
                return
            else:  # quadratic probing
                idx = (idx + i * i) % self.size
                i += 1
                if i > self.size:  # full cycle
                    raise Exception("HashTable is full")

    # ---- Search with quadratic probing ----
    def search(self, key):
        idx = self._hash(key)
        i = 1
        while True:
            slot = self.table[idx]
            if slot is None:  #empty means not found
                return None
            if slot != "DELETED" and slot.key == key:
                return slot.value
            idx = (idx + i * i) % self.size
            i += 1
            if i > self.size:
                return None

    # --- Delete with quadratic probing ---
    def delete(self, key):
        idx = self._hash(key)
        i = 1
        while True:
            slot = self.table[idx]
            if slot is None:
                return False
            if slot != "DELETED" and slot.key == key:
                self.table[idx] = "DELETED"
                self.count -= 1
                return True
            idx = (idx + i * i) % self.size
            i += 1
            if i > self.size:
                return False

    # >> Rehashing
    def _rehash(self, new_size):
        old_table = self.table
        self.size = new_size
        self.table = [None] * self.size
        self.count = 0
        for slot in old_table:
            if slot is not None and slot != "DELETED":
                self.insert(slot.key, slot.value)

    # Helpers: Prime table sizes
    def _is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def _next_prime(self, n):
        while not self._is_prime(n):
            n += 1
        return n


# Test
ht = HashTable(size=7, threshold=0.7)
ht.insert(50, 'A')
ht.insert(700, 'B')
ht.insert(76, 'C')
ht.insert(85, 'D')
ht.insert(92, 'E')

print("Search 92 ->", ht.search(92))
ht.delete(76)
print("Search 76 ->", ht.search(76))
