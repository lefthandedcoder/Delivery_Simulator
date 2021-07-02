class HashTable:
    def __init__(self):
        self.size = 7
        self.table = [None] * self.size
        self.n = 0
        self.max_load_factor = 0.75

    def get_hash(self, key):
        if isinstance(key, int):
            return int(key) % len(self.table)
        else:
            return ord(key[0]) % len(self.table)

    def add(self, key, value):
        key_hash = self.get_hash(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            # Fills empty slot
            self.table[key_hash] = list([key_value])
            self.n += 1
            if float(self.n / len(self.table) > self.max_load_factor):
                self.resize(2 * len(self.table) - 1)
            return True
        else:
            # Updates key/value pair
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            # Adds to chained list for slot
            self.table[key_hash].append(key_value)
            self.n += 1
            return True

    # Gets value from hash table
    def get(self, key):
        # Finds slot
        key_hash = self.get_hash(key)
        # Finds value if key is in slot
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    # Deletes value from hash table
    def delete(self, key):
        key_hash = self.get(key)

        if self.table[key_hash] is None:
            return False
        for i in range (0, len(self.table[key_hash])):
            if self.table[key_hash][i][0] == key:
                self.table[key_hash].pop(i)
                return True

    def resize(self, size):
        previous_table = []
        for bucket in self.table:
            if bucket is not None:
                for pairs in bucket:
                    previous_table.append(pairs)
        self.table = [None] * size
        self.n = 0
        for pairs in previous_table:
            self.add(pairs[0], pairs[1])


    def print(self):
        for pair in self.table:
            if pair is not None:
                print(str(pair))
