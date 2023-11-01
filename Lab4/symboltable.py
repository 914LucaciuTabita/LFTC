from hashtable import HashTable


class SymbolTable:
    def __init__(self, size=100):
        self.table = HashTable(size)
        self.variable_count = 0

    def add(self, key, value=None):
        if not self.has(key):
            if value is None:
                # Only increment variable count when you are adding a new variable to the symbol table
                self.variable_count += 1
                value = self.variable_count
            self.table.add(key, value)

    def has(self, key):
        if key.endswith('$'):
            key = key[:-1]
        return self.table.contains(key)

    def get_position(self, key):
        return self.table.getPosition(key)

    def __str__(self):
        return f"Symbol Table: {self.table}"
