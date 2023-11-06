import re
# ANSI escape codes for color formatting
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"


class Scanner:
    def __init__(self, symbol_table):
        self.reserved_words = re.compile(r'tab|if_so|else|for_this|return|while|print|read|True|False')
        self.operators = re.compile(r'\+|-|\*|/|<|<=|>=|>|==|=|!=|:|;|%|$')
        self.separators = re.compile(r'\(|\)|<|>|{|}| | {4}|,')
        self.identifiers = re.compile(r'[A-Za-z_][A-Za-z0-9_]*')
        self.digits = re.compile(r'[0-9]')
        self.chars = re.compile(r"'[A-Za-z0-9]'")
        self.strings = re.compile(r'"[^"]*"')
        self.pif_table = []
        self.current_position = -1
        self.symbol_table = symbol_table

    def add_element(self, token):
        # If the token is an identifier, get its position from the Symbol Table
        if self.symbol_table.has(token):
            id = self.symbol_table.table.get_variable_count(token)
        else:
            id = -1  # Token is not an identifier

        self.pif_table.append((token, id))

    def buffering_from_file(self, input_file):
        with open(input_file, 'r') as file:
            source_code = file.read()

        return self.buffering(source_code)

    def buffering(self, source_code):
        i = 0
        line = 1

        while i < len(source_code):
            char = source_code[i]

            if char == '$':
                match = self.identifiers.match(source_code[i + 1:])
                if match:
                    token = match.group(0)
                    self.symbol_table.add(token)
                    self.add_element(token)
                    i += len(token) + 1
                else:
                    print(f"{RED}Lexical error: Invalid identifier --> {YELLOW}token: '{char}'{RED} at {YELLOW}line: {line}{RESET}")
                    i += 1

            elif char.isalpha() or char == '_':
                match = self.identifiers.match(source_code[i:])
                if match:
                    token = match.group(0)
                    self.add_element(token)
                    i += len(token)
                else:
                    print(f"{RED}Lexical error: Invalid identifier --> {YELLOW}token: '{char}'{RED} at {YELLOW}line: {line}")
                    i += 1

            elif char in "0123456789":
                match = self.digits.match(source_code[i:])
                if match:
                    token = char  # Initialize the token with the first digit
                    i += 1
                    while i < len(source_code) and source_code[i].isdigit():
                        token += source_code[i]
                        i += 1
                    if len(token) > 1 and token[0] == '0':
                        print(f"{RED}Lexical error: Invalid constant (starting with '0') --> {YELLOW}token: '{token}'{RED} at {YELLOW}line: {line}{RESET}")
                    else:
                        self.add_element(token)
                        self.symbol_table.add(token)
                else:
                    print(f"{RED}Lexical error: Invalid constant --> {YELLOW}token: '{char}'{RED} at {YELLOW}line: {line}{RESET}")
                    i += 1

            elif char == ":":
                if source_code[i + 1] == ":":
                    token = "::"
                    self.add_element(token)
                    i += 2  # Skip the 2 spaces
                else:
                    i += 1  # Skip a single space

            elif char in "+-*/<=>!:;%":
                match = self.operators.match(source_code[i:])
                if match:
                    token = match.group(0)
                    self.add_element(token)
                    i += len(token)
                else:
                    print(f"{RED}Lexical error: Invalid operator --> {YELLOW}token: '{char}'{RED} at {YELLOW}line: {line}{RESET}")
                    i += 1

            elif char in "()<{}>.,":
                match = self.separators.match(source_code[i:])
                if match:
                    token = match.group(0)
                    self.add_element(token)
                    i += len(token)
                else:
                    print(f"{RED}Lexical error: Invalid separator --> {YELLOW}token: '{char}'{RED} at {YELLOW}line: {line}{RESET}")
                    i += 1

            elif char == "'":
                match = self.chars.match(source_code[i:])
                if match:
                    token = match.group(0)
                    self.add_element(token)
                    self.symbol_table.add(token)
                    i += len(token)
                else:
                    print(f"{RED}Lexical error: Invalid character --> {YELLOW}token: '{char}'{RED} at {YELLOW}line: {line}{RESET}")
                    i += 1

            elif char == '"':
                match = self.strings.match(source_code[i:])
                if match:
                    token = match.group(0)
                    self.add_element(token)
                    self.symbol_table.add(token)
                    i += len(token)
                else:
                    print(f"{RED}Lexical error: Invalid string --> {YELLOW}token: '{char}'{RED} at {YELLOW}line: {line}{RESET}")
                    i += 1

            elif char == " ":
                # Handle the "tab" as an identifier (ID)
                if source_code[i:i + 4] == "   ":
                    token = "tab"
                    self.add_element(token)
                    i += 4  # Skip the four spaces
                else:
                    i += 1  # Skip a single space

            elif char == "#":
                if source_code[i + 1] == "#":
                    while source_code[i] != "\n":
                        i += 1

            elif char == "\n":
                line += 1
                i += 1  # Ignore newline

            else:
                print(f"{RED}Lexical error: Unknown character --> {YELLOW}token: '{char}'{RED} at {YELLOW}line: {line}{RESET}")
                i += 1

        return self.pif_table

    def get_pif_table(self):
        return self.pif_table

    def print_tables(self):
        for code, position in self.pif_table:
            print(f"{code} {position}")

        print(self.symbol_table.__str__())

    def write_tables_to_files(self, output_pif_file, output_symbol_table_file):
        with open(output_pif_file, 'w') as pif_output, open(output_symbol_table_file, 'w') as symbol_table_output:
            # Write PIF table to pif_output
            for code, position in self.pif_table:
                pif_output.write(f"{code}   | {position}\n")

            symbol_table_output.write(self.symbol_table.print_sym_table())
