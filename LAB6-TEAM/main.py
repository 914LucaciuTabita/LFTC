from Grammar import Grammar
from Item import Item
from Parser import Parser

if __name__ == '__main__':
    # Read the grammar from the file
    g = Grammar()
    g.read_from_file("g5.in")
    print(g)

    # Make the grammar enhanced
    g.make_enhanced_grammar()

    # Create and generate the parser
    parser = Parser(g)
    parser.generate_parsing_table()

    # Print the parsing table
    print("Parsing Table:")
    for nonterminal, row in parser.parsing_table.items():
        for terminal, production in row.items():
            print(f"{nonterminal} -> {terminal}: {production}")

