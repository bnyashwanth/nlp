
def minimum_edit_distance(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],
                    dp[i][j - 1],
                    dp[i - 1][j - 1]
                )

    return dp[m][n], dp


def display_table(dp, a, b):
    print("\nEdit Distance Table:")
    print("    ", *("#" + b), sep="    ")

    for i, row in enumerate(dp):
        label = "#" if i == 0 else a[i - 1]
        print(f"{label:4}", end="")
        for value in row:
            print(f"{value:<4}", end="")
        print()


tests = [
    ("kitten", "sitting"),
    ("flaw", "lawn"),
    ("intention", "execution"),
    ("apple", "aple"),
    ("", "hello"),
    ("hello", "")
]

for a, b in tests:
    print(f"\nComparing: '{a}' -> '{b}'")
    distance, dp = minimum_edit_distance(a, b)
    print("Minimum Edit Distance:", distance)
    display_table(dp, a, b)
