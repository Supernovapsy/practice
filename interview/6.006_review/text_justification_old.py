from sys import argv

"""
words
dp[0] 0..len(words) what is the next word that starts a new line?
dp[0..len(words) - 1]
"""

file_name = argv[1]
text = open(file_name).read().strip()
width = int(argv[2])
words = text.split()

def cost(min_width):
    return (width - min_width) ** 3

# Want to find dp[i] for i in (0, len(words))
# dp[i] stores the index of the next word which starts a new line.
# dp[0] gives me a value, j. This is the next word which starts a new line. dp[j] -> k...

# example: width = 10
# text: do or not do there is no try
# wordN = 8
# dp[7] = 7^3, dp[6] = 4^3, dp[5] = 1^3

dp = [(0, 0)] * (len(words) + 1)
# Solve each step of the dynamic programming approach in a topological order.
for i in reversed(xrange(len(words))):
    min_width = -1
    best_choice = (i + 1, float('inf'))
    for j in xrange(i + 1, len(words) + 1):
        min_width += 1 + len(words[j - 1])
        if min_width <= width:
            c = cost(min_width) + dp[j][1]
            if c < best_choice[1]:
                best_choice = (j, c)
        else:
            break
    dp[i] = best_choice


words_with_newlines = []
i = 0
while i != len(words):
    j = dp[i][0]
    assert j > i, "There is something wrong with dp."
    for k in xrange(i, j):
        if k != i and k != 0:
            words_with_newlines.append(words[k])
    if j != len(words):
        words_with_newlines.append(words_with_newlines.pop() + "\n" + words[j])
    i = j

print " ".join(words_with_newlines)
