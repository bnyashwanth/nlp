
from collections import defaultdict

class Parser:
    def __init__(self, grammar, start_symbol="S"):
        self.start_symbol = start_symbol
        self.rules = defaultdict(list)
        for lhs, rhs in grammar:
            self.rules[lhs].append(rhs)

    def top_down_parse(self, sentence):
        def parse(symbol, index):
            if symbol not in self.rules:
                if index < len(sentence) and sentence[index] == symbol:
                    return True, (symbol,), index + 1
                return False, None, index

            for production in self.rules[symbol]:
                new_index, children, success = index, [], True

                for sym in production:
                    success, subtree, new_index = parse(sym, new_index)
                    if not success:
                        break
                    children.append(subtree)

                if success:
                    return True, (symbol, children), new_index

            return False, None, index

        success, tree, index = parse(self.start_symbol, 0)
        return tree if success and index == len(sentence) else None

    def bottom_up_parse(self, sentence):
        stack, input_buffer, steps = [], sentence[:], []

        while True:
            if stack == [self.start_symbol] and not input_buffer:
                return steps + [("ACCEPT", stack[:], input_buffer[:])]

            if input_buffer:
                stack.append(input_buffer.pop(0))
                steps.append(("SHIFT", stack[:], input_buffer[:]))

            reduced = True
            while reduced:
                reduced = False
                for lhs, rhs_list in self.rules.items():
                    for rhs in rhs_list:
                        if len(stack) >= len(rhs) and stack[-len(rhs):] == rhs:
                            stack[-len(rhs):] = [lhs]
                            steps.append(
                                (f"REDUCE {lhs}->{rhs}", stack[:], input_buffer[:])
                            )
                            reduced = True
                            break
                    if reduced:
                        break

            if not input_buffer and stack != [self.start_symbol]:
                return steps + [("REJECT", stack[:], input_buffer[:])]


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

print("Top-Down Parse Tree:")
print(parser.top_down_parse(sentence))

print("\nBottom-Up Parsing Steps:")
for action, stack, input_buffer in parser.bottom_up_parse(sentence):
    print(f"{action:15} | Stack: {stack} | Buffer: {input_buffer}")
