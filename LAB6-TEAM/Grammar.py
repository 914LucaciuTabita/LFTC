class Grammar:
    EPSILON = "epsilon"
    STARTING_SYMBOL = "S'"

    def __init__(self, is_enhanced=False):
        self.N = []
        self.E = []
        self.S = ""
        self.P = {}
        self.is_enhanced = is_enhanced

    def check_if_grammar_is_enhanced(self):
        # check that the starting symbol has only one production
        if len(self.P[self.S]) != 1:
            return False
        # check that the starting symbol does not appear on the right hand side of any production
        for production in self.P.values():
            for rhs in production:
                if self.S in rhs:
                    return False
        return True

    def make_enhanced_grammar(self):
        if not self.is_enhanced:
            # add a new non-terminal symbol S'
            self.N.append(Grammar.STARTING_SYMBOL)
            # add a new production S' -> S
            self.P[Grammar.STARTING_SYMBOL] = [[self.S]]
            # change the starting symbol to Z
            self.S = Grammar.STARTING_SYMBOL
            self.is_enhanced = True

    def FIRST(self, symbol):
        if symbol in self.E:
            return {symbol}
        elif symbol in self.N:
            first_set = set()
            for production in self.P[symbol]:
                first_set |= (set(self.FIRST(production[0])) - {self.EPSILON})
                if self.EPSILON not in self.FIRST(production[0]):
                    break
            return first_set
        else:
            return {symbol}  # For terminals

    def FOLLOW(self, symbol, processing=None):
        if processing is None:
            processing = set()

        if symbol == self.S:
            return {'$'}

        follow_set = set()

        if symbol not in self.N:
            return follow_set  # For terminals

        if symbol in processing:
            return follow_set  # Avoid infinite recursion

        processing.add(symbol)

        for nonterminal in self.N:
            for production in self.P[nonterminal]:
                for i, current_symbol in enumerate(production):
                    if current_symbol == symbol:
                        if i < len(production) - 1:
                            follow_set |= self.FIRST(production[i + 1]) - {self.EPSILON}
                            if self.EPSILON in self.FIRST(production[i + 1]):
                                follow_set |= self.FOLLOW(nonterminal, processing)
                        elif nonterminal != symbol:
                            follow_set |= self.FOLLOW(nonterminal, processing)

        processing.remove(symbol)

        return follow_set

    @staticmethod
    def __process_line(line: str):
        # Get what comes after the '='
        return line.strip().split(' ')[2:]

    def read_from_file(self, file_name: str):
        with open(file_name) as file:
            N = self.__process_line(file.readline())
            E = self.__process_line(file.readline())
            S = self.__process_line(file.readline())[0]

            file.readline()  # P =
            # Get all transitions
            P = {}
            for line in file:
                split = line.strip().split('->')
                source = split[0].strip()
                sequence = split[1].lstrip(' ')
                sequence_list = []
                for c in sequence.split(' '):
                    sequence_list.append(c)

                if source in P.keys():
                    P[source].append(sequence_list)
                else:
                    P[source] = [sequence_list]

            self.N = N
            self.E = E
            self.S = S
            self.P = P

    def check_cfg(self):
        has_starting_symbol = False
        for key in self.P.keys():
            if key == self.S:
                has_starting_symbol = True
            if key not in self.N:
                return False
        if not has_starting_symbol:
            return False
        for production in self.P.values():
            for rhs in production:
                for value in rhs:
                    if value not in self.N and value not in self.E and value != Grammar.EPSILON:
                        return False
        return True

    def __str__(self):
        result = "N = " + str(self.N) + "\n"
        result += "E = " + str(self.E) + "\n"
        result += "S = " + str(self.S) + "\n"
        result += "P = " + str(self.P) + "\n"
        return result