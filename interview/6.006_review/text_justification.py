from sys import argv

def cost(length, width):
    if length <= width:
        return (width - length)**3
    return float('inf')

def dp(words, i, width, mem):
    if len(words[i]) > width:
        raise Exception("a word is longer than the width of the page!")
    min_cost = float("inf")
    min_j = 0
    length = -1
    for j in range(i + 1, len(words) + 1):
        length += len(words[j - 1]) + 1
        if length > width:
            break
        candidate_cost = cost(length, width) + mem[j][0]
        if candidate_cost < min_cost:
            min_cost = candidate_cost
            min_j = j
    mem[i]= min_cost, min_j

def justify(text, width):
    words = text.split()
    mem = [(None, None)] * (len(words) + 1)
    mem[-1] = 0, len(words)
    for i in reversed(range(len(words))):
        dp(words, i, width, mem)

    ret = []
    i = 0
    while i < len(words):
        ret.append(" ".join(words[i:mem[i][1]]))
        i = mem[i][1]
    return "\n".join(ret)

if __name__ == "__main__":
    file_name = argv[1]
    text = open(file_name).read().strip()
    line_width = int(argv[2])
    justified_text = justify(text, line_width)
    print justified_text
