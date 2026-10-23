
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


# Top-Down Parser
def top_down_parse(symbol, sentence, index=0):
    if symbol not in dict((lhs, None) for lhs, rhs in grammar):
        if index < len(sentence) and sentence[index] == symbol:
            return True, (symbol,), index + 1
        return False, None, index

    for lhs, rhs in grammar:
        if lhs == symbol:
            children = []
            pos = index

            for item in rhs:
                success, tree, pos = top_down_parse(
                    item, sentence, pos
                )
                if not success:
                    break
                children.append(tree)
            else:
                return True, (symbol, children), pos

    return False, None, index


# Bottom-Up Parser
def bottom_up_parse(sentence):
    stack = []
    buffer = sentence.copy()

    while True:
        if stack == ["S"] and not buffer:
            print("ACCEPT")
            return

        if buffer:
            stack.append(buffer.pop(0))
            print(f"SHIFT           | Stack: {stack} | Buffer: {buffer}")

        changed = True
        while changed:
            changed = False

            for lhs, rhs in grammar:
                if len(stack) >= len(rhs) and stack[-len(rhs):] == rhs:
                    stack = stack[:-len(rhs)] + [lhs]
                    print(
                        f"REDUCE {lhs}->{rhs} | "
                        f"Stack: {stack} | Buffer: {buffer}"
                    )
                    changed = True
                    break

        if not buffer and stack != ["S"]:
            print(f"REJECT          | Stack: {stack} | Buffer: {buffer}")
            return


# Main Program
sentence = ["the", "cat", "chases", "a", "dog"]

success, tree, index = top_down_parse("S", sentence)

print("Top-Down Parse Tree:")
print(tree if success and index == len(sentence) else "Rejected")

print("\nBottom-Up Parsing Steps:")
bottom_up_parse(sentence)
