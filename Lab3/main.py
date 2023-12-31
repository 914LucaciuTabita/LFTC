from symboltable import SymbolTable

if __name__ == "__main__":
    symbol_table = SymbolTable(size=77)
    pos = (-1, -1)
    pos2 = (-1, -1)
    pos3 = (-1, -1)
    try:
        pos = symbol_table.add("apple")
        print(f"apple {pos}")
        print(f"banana {symbol_table.add('banana')}")
        print(f"cherry {symbol_table.add('cherry')}")
        print(f"date {symbol_table.add('date')}")
        print(f"elderberry {symbol_table.add('elderberry')}")

        print(f"2 {symbol_table.add(2)}")
        print(f"5 {symbol_table.add(5)}")
        pos2 = symbol_table.add(50)
        print(f"50 {pos2}")
        print(f"77 {symbol_table.add(77)}")
        print(f"111 {symbol_table.add(111)}")
        print(f"154 {symbol_table.add(154)}")
        print(f"231 {symbol_table.add(231)}")
        print(f"95 {symbol_table.add(95)}")

        print(f"str1 {symbol_table.add('str1')}")
        print(f"str2 {symbol_table.add('str2')}")
        print(f"str3 {symbol_table.add('str3')}")
        print(f"str4 {symbol_table.add('str4')}")
        pos3 = symbol_table.add("str5")
        print(f"str5 {pos3}")

        print(f"apple {symbol_table.add('apple')}")
    except Exception as e:
        print(e)

    print(symbol_table)

    try:
        assert symbol_table.has("apple") == pos, f"apple does not have position {pos}"
        assert symbol_table.getPosition(50) == pos2, f"50 does not have position {pos2}"
        assert symbol_table.getPosition("str5") == pos3, f"str5 does not have position {pos3}"
        assert symbol_table.has("aaaa") == (-1, -1), "aaaa exists in the table"
        assert symbol_table.getPosition(95) == (2, 2), "95 does not have position (2, 2)"
    except AssertionError as e:
        print(e)

    try:
        print(f"77 {symbol_table.getPosition(77)}")
        assert symbol_table.getPosition(77) == (2, 2), "77 does not have position (2, 2)"
    except AssertionError as e:
        print(e)

    try:
        print(f"elderberry {symbol_table.has('elderberry')}")
        assert symbol_table.has('elderberry') == pos, f"elderberry does not have position {pos}"
    except AssertionError as e:
        print(e)

