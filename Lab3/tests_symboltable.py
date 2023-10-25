import pytest
from symboltable import SymbolTable


def test_symbol_table():
    symbol_table = SymbolTable(size=77)
    pos = (-1, -1)
    pos2 = (-1, -1)
    pos3 = (-1, -1)

    pos = symbol_table.add("apple")
    assert symbol_table.has("apple") == pos, f"apple does not have position {pos}"
    assert symbol_table.getPosition("apple") == pos, f"apple does not have position {pos}"

    assert symbol_table.has("banana") == (0, 0), "banana does not have position (0, 0)"
    assert symbol_table.getPosition("banana") == (0, 0), "banana does not have position (0, 0)"

    assert symbol_table.has("cherry") == (0, 1), "cherry does not have position (0, 1)"
    assert symbol_table.getPosition("cherry") == (0, 1), "cherry does not have position (0, 1)"

    assert symbol_table.has("date") == (0, 2), "date does not have position (0, 2)"
    assert symbol_table.getPosition("date") == (0, 2), "date does not have position (0, 2)"

    assert symbol_table.has("elderberry") == (0, 3), "elderberry does not have position (0, 3)"
    assert symbol_table.getPosition("elderberry") == (0, 3), "elderberry does not have position (0, 3)"

    assert symbol_table.has(2) == (1, 0), "2 does not have position (1, 0)"
    assert symbol_table.getPosition(2) == (1, 0), "2 does not have position (1, 0)"

    assert symbol_table.has(5) == (1, 1), "5 does not have position (1, 1)"
    assert symbol_table.getPosition(5) == (1, 1), "5 does not have position (1, 1)"

    pos2 = symbol_table.add(50)
    assert symbol_table.has(50) == pos2, f"50 does not have position {pos2}"
    assert symbol_table.getPosition(50) == pos2, f"50 does not have position {pos2}"

    assert symbol_table.has(77) == (1, 2), "77 does not have position (1, 2)"
    assert symbol_table.getPosition(77) == (1, 2), "77 does not have position (1, 2)"

    assert symbol_table.has(111) == (2, 0), "111 does not have position (2, 0)"
    assert symbol_table.getPosition(111) == (2, 0), "111 does not have position (2, 0)"

    assert symbol_table.has(154) == (2, 1), "154 does not have position (2, 1)"
    assert symbol_table.getPosition(154) == (2, 1), "154 does not have position (2, 1)"

    assert symbol_table.has(231) == (2, 2), "231 does not have position (2, 2)"
    assert symbol_table.getPosition(231) == (2, 2), "231 does not have position (2, 2)"

    assert symbol_table.has(95) == (2, 3), "95 does not have position (2, 3)"
    assert symbol_table.getPosition(95) == (2, 3), "95 does not have position (2, 3)"

    assert symbol_table.has('str1') == (3, 0), "str1 does not have position (3, 0)"
    assert symbol_table.getPosition('str1') == (3, 0), "str1 does not have position (3, 0)"

    assert symbol_table.has('str2') == (3, 1), "str2 does not have position (3, 1)"
    assert symbol_table.getPosition('str2') == (3, 1), "str2 does not have position (3, 1)"

    assert symbol_table.has('str3') == (3, 2), "str3 does not have position (3, 2)"
    assert symbol_table.getPosition('str3') == (3, 2), "str3 does not have position (3, 2)"

    assert symbol_table.has('str4') == (3, 3), "str4 does not have position (3, 3)"
    assert symbol_table.getPosition('str4') == (3, 3), "str4 does not have position (3, 3)"

    pos3 = symbol_table.add("str5")
    assert symbol_table.has("str5") == pos3, f"str5 does not have position {pos3}"
    assert symbol_table.getPosition("str5") == pos3, f"str5 does not have position {pos3}"

    assert symbol_table.has("aaaa") == (-1, -1), "aaaa exists in the table"
    assert symbol_table.getPosition("aaaa") == (-1, -1), "aaaa exists in the table"

    assert symbol_table.has("nonexistent") == (-1, -1), "nonexistent exists in the table"
    assert symbol_table.getPosition("nonexistent") == (-1, -1), "nonexistent exists in the table"


if __name__ == '__main__':
    pytest.main()