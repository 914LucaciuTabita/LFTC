from symboltable import SymbolTable
import re


reserved_word_pattern = re.compile(r'tab|if_so|else|for_this|return|while|print|read')
operator_pattern = re.compile(r'\+|-|\*|/|<|<=|>=|>|=|!=|==|:|;|%')
separator_pattern = re.compile(r'\(|\)|<|>|{|}| | {4}|,')
identifier_pattern = re.compile(r'[A-Za-z_][A-Za-z0-9_]*')
digit_pattern = re.compile(r'[0-9]')
char_literal_pattern = re.compile(r"'[A-Za-z0-9]'")
string_literal_pattern = re.compile(r'"[^"]*"')

symbol_table = SymbolTable()
fip_table = []
current_position = -1


def add_token_to_fip(token, symbol_table):
    # If the token is an identifier, get its position from the Symbol Table
    if symbol_table.has(token):
        id = symbol_table.table.getVariableCount(token)
    else:
        id = -1  # Token is not an identifier

    fip_table.append((token, id))


def lexical_analysis(source_code, symbol_table):
    i = 0

    while i < len(source_code):
        char = source_code[i]

        if char.isalpha() or char == '_':
            match = identifier_pattern.match(source_code[i:])
            if match:
                token = match.group(0)
                if source_code[i + len(token)] == "$":
                    # Handle variable declaration
                    i += len(token)  # Move past the identifier
                    i += 1  # Move past the colon
                    symbol_table.add(token)
                    add_token_to_fip(token, symbol_table)
                else:
                    add_token_to_fip(token, symbol_table)
                i += len(token)
            else:
                print("Lexical error: Invalid identifier")
                i += 1

        elif char in "0123456789":
            match = digit_pattern.match(source_code[i:])
            if match:
                token = match.group(0)
                add_token_to_fip(token, symbol_table)
                symbol_table.add(token)
                i += len(token)
            else:
                print("Lexical error: Invalid constant")
                i += 1

        elif char in "+-*/<=>!:;%":
            match = operator_pattern.match(source_code[i:])
            if match:
                token = match.group(0)
                add_token_to_fip(token, symbol_table)
                i += len(token)
            else:
                print("Lexical error: Invalid operator")
                i += 1

        elif char in "()<{}>.,":
            match = separator_pattern.match(source_code[i:])
            if match:
                token = match.group(0)
                add_token_to_fip(token, symbol_table)
                i += len(token)
            else:
                print("Lexical error: Invalid separator")
                i += 1

        elif char == "'":
            match = char_literal_pattern.match(source_code[i:])
            if match:
                token = match.group(0)
                add_token_to_fip(token, symbol_table)
                symbol_table.add(token)
                i += len(token)
            else:
                print("Lexical error: Invalid character")
                i += 1

        elif char == '"':
            match = string_literal_pattern.match(source_code[i:])
            if match:
                token = match.group(0)
                add_token_to_fip(token, symbol_table)
                symbol_table.add(token)
                i += len(token)
            else:
                print("Lexical error: Invalid string")
                i += 1

        elif char == " ":
            # Handle the "tab" as an identifier (ID)
            if source_code[i:i + 4] == "    ":
                token = "    "
                add_token_to_fip(token, symbol_table)
                i += 4  # Skip the three spaces
            else:
                i += 1  # Skip a single space

        elif char == "#":
            if source_code[i+1] == "#":
                while source_code[i] != "\n":
                    i += 1

        elif char == "\n":
            i += 1  # Ignore newline

        else:
            print(f"Lexical error: Unknown character '{char}'")
            i += 1

    return fip_table


def write_to_output_files(fip_file, symbol_table_file, fip_table, symbol_table):
    with open(fip_file, 'w') as fip_output, open(symbol_table_file, 'w') as symbol_table_output:
        # Write FIP table to fip_file
        fip_output.write("Position in ST |   Cod atom\n")
        for code, position in fip_table:
            fip_output.write(f"       {position}      |   {code}\n")

        # Write Symbol Table to symbol_table_file
        symbol_table_output.write("Position | Atom lexical\n")
        position = 1
        for key in symbol_table.table.table:
            if key is not None:
                value = symbol_table.table.getVariableCount(key[0])
                symbol_table_output.write(f"    {position}    |     {key[0]}\n")
                position += 1


def read_source_code(input_file):
    with open(input_file, 'r') as file:
        source_code = file.read()
    return source_code

