
class HashTable:
    def __init__(self, capacity=10):
        self.table = [None] * capacity

    # Get hash key, O(1)
    def _get_hash(self, key):
        return int(key) % len(self.table)

    # Add packages to hash table, O(n)
    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            # Creates linked list
            self.table[key_hash].append(key_value)
            return True

    # Gets value from hash table -> O(n)
    def get(self, key):
        key_hash = self._get_hash(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    # Deletes value from hash table -> O(n)
    def delete(self, key):
        key_hash = self._get_hash(key)

        if self.table[key_hash] is None:
            return False
        for i in range (0, len(self.table[key_hash])):
            if self.table[key_hash][i][0] == key:
                self.table[key_hash].pop(i)
                return True

    def print(self):
        for item in self.table:
            if item is not None:
                print(str(item))
