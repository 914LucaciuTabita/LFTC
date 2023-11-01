from symboltable import SymbolTable
from scanner import lexical_analysis, fip_table, read_source_code, write_to_output_files


if __name__ == "__main__":
    symbol_table = SymbolTable(size=100)

    output_fip_file = "output_fip.txt"
    output_symbol_table_file = "output_symbol_table.txt"

    source_code = read_source_code("p2.txt")
    lexical_analysis(source_code, symbol_table)
    write_to_output_files(output_fip_file, output_symbol_table_file, fip_table, symbol_table)
    print("FIP Table:")
    for code, position in fip_table:
        print(f"{code} |  {position}")

    print("\nSymbol Table:")
    print(symbol_table.__str__())
