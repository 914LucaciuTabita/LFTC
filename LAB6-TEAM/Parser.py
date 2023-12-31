from collections import defaultdict
from typing import Set
from Item import Item
from Grammar import Grammar
from ParseTreeNode import ParseTreeNode
from State import State

class Parser:
    def __init__(self, grammar: Grammar):
        self.grammar = grammar
        self.parsing_table = {}
        self.parse_tree_root = None
        self.current_parse_tree_node = None

    def generate_parsing_table(self):
        try:
            if not self.grammar.check_cfg():
                raise ValueError("Grammar is not Context-Free.")
        except ValueError as e:
            print(f"Error: {e}")
            return

        self.parsing_table = defaultdict(dict)

        for nonterminal in self.grammar.non_terminals:
            for terminal in self.grammar.terminals:
                if terminal != Grammar.EPSILON:
                    self.parsing_table[nonterminal][terminal] = self.find_production(nonterminal, terminal)

            if Grammar.EPSILON in self.grammar.FIRST(nonterminal):
                for terminal in self.grammar.FOLLOW(nonterminal):
                    self.parsing_table[nonterminal][terminal] = self.find_production(nonterminal, terminal)

            if Grammar.EPSILON in self.grammar.FOLLOW(nonterminal) and '$' in self.grammar.FOLLOW(nonterminal):
                self.parsing_table[nonterminal]['$'] = self.find_production(nonterminal, '$')

    def find_production(self, nonterminal: str, terminal: str) -> list:
        productions = self.grammar.productions[nonterminal]
        for production in productions:
            first_set = self.grammar.FIRST(production[0])
            if terminal in first_set:
                return production
            if Grammar.EPSILON in first_set:
                follow_set = self.grammar.FOLLOW(nonterminal)
                if terminal in follow_set:
                    return production
        return None

    def parse(self, input_string: str) -> bool:
        stack = [ParseTreeNode('$')]
        input_tokens = list(input_string) + ['$']
        current_input = input_tokens[0]
        stack_top = stack[-1]

        self.parse_tree_root = stack_top
        self.current_parse_tree_node = stack_top

        while stack_top.value != '$':
            if stack_top.value in self.grammar.non_terminals:
                if current_input in self.parsing_table[stack_top.value]:
                    production = self.parsing_table[stack_top.value][current_input]
                    stack.pop()
                    if production[0] != Grammar.EPSILON:
                        for symbol in reversed(production):
                            new_node = ParseTreeNode(symbol)
                            self.current_parse_tree_node.add_child(new_node)
                            if self.current_parse_tree_node.children:
                                sibling = self.current_parse_tree_node.children[0]
                                while sibling.sibling:
                                    sibling = sibling.sibling
                                sibling.add_sibling(new_node)
                            self.current_parse_tree_node = new_node
                            stack.append(new_node)
                else:
                    return False
            elif stack_top.value == current_input:
                stack.pop()
                input_tokens.pop(0)
                self.current_parse_tree_node = self.current_parse_tree_node.father
            else:
                return False

            stack_top = stack[-1]
            current_input = input_tokens[0]

        return True

    def print_parse_tree(self):
        if self.parse_tree_root:
            print(self.parse_tree_root.__str__())