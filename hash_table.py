class HashTable:
    def __init__(self):
        self.size = 7
        self.table = [None] * self.size
        # Keeps track of elements in table
        self.n = 0
        # Load factor that determines whether or not the table should be resized
        self.max_load_factor = 0.75

    # Checks if key is an integer or a string O(1)
    def get_hash(self, key):
        if isinstance(key, int):
            return int(key) % len(self.table)
        else:
            return ord(key[0]) % len(self.table)

    # Adds key-value pair to hash table
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
            # Updates key/value pair, O(n)
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
            # Goes through pairs in table, finds key, and retries value, O(n)
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    # Deletes value from hash table
    def delete(self, key):
        key_hash = self.get(key)

        if self.table[key_hash] is None:
            return False
        # Deletes key-value pair from table, O(n)
        for i in range(0, len(self.table[key_hash])):
            if self.table[key_hash][i][0] == key:
                self.table[key_hash].pop(i)
                return True

    def resize(self, size):
        previous_table = []
        # Retrieves key-value pairs from current table and stores in new 'previous' list
        for bucket in self.table:
            if bucket is not None:
                for pairs in bucket:
                    previous_table.append(pairs)
        # Builds table with new size (2 * previous_size - 1), the -1 gives a greater chance for a prime number, and thus
        # less chance that the mod function will unnecessarily store multiple elements in a single bucket
        self.table = [None] * size
        # Resets element counter
        self.n = 0
        # Goes through previous elements and adds them to the newly built table
        for pairs in previous_table:
            self.add(pairs[0], pairs[1])

    # Prints out all values in the table, O(n)
    def print(self):
        # Goes through all slots in table and finds ones with elements and prints their values
        for pair in self.table:
            if pair is not None:
                print(str(pair))
