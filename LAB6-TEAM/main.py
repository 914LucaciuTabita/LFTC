from Grammar import Grammar
from Item import Item
from Parser import Parser


def menu(gr):
    while True:
        inp = input(">")
        if inp == "1":
            print(gr.non_terminals)
        elif inp == "2":
            print(gr.terminals)
        elif inp == "3":
            print(gr.starting_nt)
        elif inp == "4":
            print(gr.productions)
        elif inp == "5":
            print(gr.cfg_check())
        elif inp == "0":
            break
        else:
            print("Invalid action!")


def print_menu():
    print("1. Print the set of non-terminals\n"
          "2. Print the set of terminals\n"
          "3. Print the starting non-terminal\n"
          "4. Print the productions\n"
          "5. Check if the grammar is context-free\n"
          "0. Exit\n\n")


if __name__ == '__main__':
    # Read the grammar from the file
    g = Grammar()
    g.read_from_file("g1.in")
    # print(g)

    print_menu()
    menu(g)

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

