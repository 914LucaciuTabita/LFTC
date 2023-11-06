from symboltable import SymbolTable
from scanner import Scanner

if __name__ == "__main__":
    symbol_table = SymbolTable(size=77)

    output_pif_file = "output_pif.txt"
    output_symbol_table_file = "output_symbol_table.txt"

    scanner = Scanner(symbol_table)
    scanner.buffering_from_file("p1err.txt")  # examples of files: p1.txt, p2.txt, p3.txt, p1err.txt, CodeBeingRead
    print("\n")
    print("PIF Table:")
    for code, position in scanner.get_pif_table():
        print(f"{code}   |  {position}")

    print("\n")
    print(symbol_table.__str__())

    print("\n")
    print(symbol_table.print_sym_table())

    scanner.write_tables_to_files("output_pif.txt", "output_symbol_table.txt")
