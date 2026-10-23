```python
class Parser:
    def __init__(self, grammar, start="S"):
        self.rules = {}
        self.start = start
        for lhs, rhs in grammar:
            self.rules.setdefault(lhs, []).append(rhs)

    def top_down_parse(self, sentence):
        def parse(sym, i):
            if sym not in self.rules:
                return ((sym,), i + 1) if i < len(sentence) and sentence[i] == sym else (None, i)

            for rhs in self.rules[sym]:
                children, j = [], i
                for s in rhs:
                    tree, j = parse(s, j)
                    if tree is None:
                        break
                    children.append(tree)
                else:
                    return ((sym, children), j)
            return None, i

        tree, i = parse(self.start, 0)
        return tree if i == len(sentence) else None

    def bottom_up_parse(self, sentence):
        stack, buf, steps = [], sentence.copy(), []

        while True:
            if stack == [self.start] and not buf:
                steps.append(("ACCEPT", stack.copy(), buf.copy()))
                return steps

            if buf:
                stack.append(buf.pop(0))
                steps.append(("SHIFT", stack.copy(), buf.copy()))

            while True:
                for lhs, rhss in self.rules.items():
                    for rhs in rhss:
                        if len(stack) >= len(rhs) and stack[-len(rhs):] == rhs:
                            stack = stack[:-len(rhs)] + [lhs]
                            steps.append((f"REDUCE {lhs}->{rhs}", stack.copy(), buf.copy()))
                            break
                    else:
                        continue
                    break
                else:
                    break

            if not buf and stack != [self.start]:
                steps.append(("REJECT", stack.copy(), buf.copy()))
                return steps


grammar = [
    ("S", ["NP", "VP"]), ("NP", ["Det", "N"]),
    ("VP", ["V", "NP"]), ("VP", ["V"]),
    ("Det", ["a"]), ("Det", ["the"]),
    ("N", ["cat"]), ("N", ["dog"]),
    ("V", ["chases"]), ("V", ["eats"])
]

parser = Parser(grammar)
sentence = ["the", "cat", "chases", "a", "dog"]

print("Top-Down Parse Tree:")
print(parser.top_down_parse(sentence))

print("\nBottom-Up Parsing Steps:")
for action, stack, buffer in parser.bottom_up_parse(sentence):
    print(f"{action:15} | Stack: {stack} | Buffer: {buffer}")
```