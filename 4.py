class Parser:
    def __init__(self, grammar, start_symbol="S"):
        self.grammar = grammar
        self.start_symbol = start_symbol
        self.rules = self._build_rules(grammar)

    def _build_rules(self, grammar):
        rules = {}
        for lhs, rhs in grammar:
            if lhs not in rules:
                rules[lhs] = []
            rules[lhs].append(rhs)
        return rules

    def top_down_parse(self, sentence):
        success, tree, index = self._top_down_helper(
            self.start_symbol, sentence, 0
        )
        if success and index == len(sentence):
            return tree
        return None

    def _top_down_helper(self, symbol, sentence, index):
        if symbol not in self.rules:
            if index < len(sentence) and sentence[index] == symbol:
                return True, (symbol,), index + 1
            return False, None, index

        for production in self.rules[symbol]:
            children = []
            new_index = index
            success = True

            for sym in production:
                success, subtree, new_index = self._top_down_helper(
                    sym, sentence, new_index
                )
                if not success:
                    break
                children.append(subtree)

            if success:
                return True, (symbol, children), new_index

        return False, None, index

    def bottom_up_parse(self, sentence):
        stack = []
        input_buffer = sentence.copy()
        steps = []

        while True:
            if stack == [self.start_symbol] and not input_buffer:
                steps.append(("ACCEPT", stack.copy(), input_buffer.copy()))
                return steps

            if input_buffer:
                word = input_buffer.pop(0)
                stack.append(word)
                steps.append(("SHIFT", stack.copy(), input_buffer.copy()))

            reduced = True
            while reduced:
                reduced = False
                for lhs, rhs_list in self.rules.items():
                    for rhs in rhs_list:
                        if len(stack) >= len(rhs) and stack[-len(rhs):] == rhs:
                            stack = stack[:-len(rhs)] + [lhs]
                            steps.append((
                                f"REDUCE {lhs}->{rhs}",
                                stack.copy(),
                                input_buffer.copy()
                            ))
                            reduced = True
                            break
                    if reduced:
                        break

            if not input_buffer and stack != [self.start_symbol]:
                steps.append(("REJECT", stack.copy(), input_buffer.copy()))
                return steps


grammar = [
    ("S", ["NP", "VP"]),
    ("NP", ["Det", "N"]),
    ("VP", ["V", "NP"]),
    ("VP", ["V"]),
    ("Det", ["a"]),
    ("Det", ["the"]),
    ("N", ["cat"]),
    ("N", ["dog"]),
    ("V", ["chases"]),
    ("V", ["eats"])
]

parser = Parser(grammar)

sentence = ["the", "cat", "chases", "a", "dog"]

top_down_result = parser.top_down_parse(sentence)
print("Top-Down Parse Tree:")
print(top_down_result)

print("\nBottom-Up Parsing Steps:")
steps = parser.bottom_up_parse(sentence)

for action, stack, buffer in steps:
    print(f"{action:15} | Stack: {stack} | Buffer: {buffer}")
