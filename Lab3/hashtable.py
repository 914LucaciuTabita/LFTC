class HashTable:
    def __init__(self, size=100, load_factor=0.7):
        self.size = size
        self.load_factor = load_factor
        self.table = [None] * self.size
        self.count = 0

    def resize(self, new_size):
        old_table = self.table
        self.size = new_size
        self.table = [None] * self.size
        self.count = 0
        for entry in old_table:
            if entry is not None:
                for key, value in entry:
                    self.add(key, value)

    def hash(self, key):
        if isinstance(key, int):
            return key % self.size
        elif isinstance(key, str):
            return sum(ord(char) for char in key) % self.size
        else:
            raise ValueError("Unsupported key type")

    def getSize(self):
        return self.size

    def getHashValue(self, key):
        return self.hash(key)

    def add(self, key, value=None):
        if self.count / self.size >= self.load_factor:
            self.resize(2 * self.size)

        index = self.hash(key)
        if self.table[index] is None:
            self.table[index] = []
        for i, entry in enumerate(self.table[index]):
            if entry[0] == key:
                if value is not None:
                    self.table[index][i] = (key, value)
                return (index, i)
        self.table[index].append((key, value))
        self.count += 1
        return (index, len(self.table[index]) - 1)

    def contains(self, key):
        index = self.hash(key)
        if self.table[index] is not None:
            for entry in self.table[index]:
                if entry[0] == key:
                    return True
        return False

    def getPosition(self, key):
        index = self.hash(key)
        if self.table[index] is not None:
            for i, entry in enumerate(self.table[index]):
                if entry[0] == key:
                    return (index, i)
        return (-1, -1)

    def __str__(self):
        return str(self.table)
