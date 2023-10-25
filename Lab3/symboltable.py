from hashtable import HashTable


class SymbolTable:
    def __init__(self, size=100):
        self.table = HashTable(size)

    def add(self, key, value=None):
        return self.table.add(key, value)

    def has(self, key):
        return self.table.contains(key)

    def getPosition(self, key):
        return self.table.getPosition(key)

    def __str__(self):
        return f"Symbol Table: {self.table}"