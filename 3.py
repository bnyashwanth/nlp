def minimum_edit_distance(str1, str2):
    m, n = len(str1), len(str2)

    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i

    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],
                    dp[i][j - 1],
                    dp[i - 1][j - 1]
                )

    return dp[m][n], dp


def display_edit_distance_table(dp, str1, str2):
    print("\nEdit Distance Table:")
    print("  " + " ".join("#" + c for c in " " + str2))

    for i, row in enumerate(dp):
        prefix = "#" if i == 0 else str1[i - 1]
        print(f"{prefix} {' '.join(map(str, row))}")


def test_med():
    test_cases = [
        ("kitten", "sitting"),
        ("flaw", "lawn"),
        ("intention", "execution"),
        ("apple", "aple"),
        ("", "hello"),
        ("hello", "")
    ]

    for str1, str2 in test_cases:
        print(f"\nComparing: '{str1}' -> '{str2}'")
        med, dp = minimum_edit_distance(str1, str2)
        print(f"Minimum Edit Distance: {med}")
        display_edit_distance_table(dp, str1, str2)


test_med()
