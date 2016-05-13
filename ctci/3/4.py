from sys import argv

def push(stack, value):
    if len(stack) == 0 or stack[-1] > value:
        stack.append(value)
        return True
    return False

def pop(stack):
    return stack.pop()

def display_stacks(stacks):
    print '----begin----'
    for stack in stacks:
        print " ".join([str(ele) for ele in stack])
    print '-----end-----'

N = int(argv[1])

stacks = [list(reversed(range(1, N + 1))), [], []]

def play_hanoi(moves):
    for pop_move, push_move in moves:
        value = pop(stacks[pop_move])
        if not push(stacks[push_move], value):
            raise Exception("Push failed. Tried to put %d in stack %d" %
            (value, push_move))
        display_stacks(stacks)

soln = [(0, 1), (1, 2)]
for i in range(1, N):
    soln += [(0, 1)] + [(j, i) for i, j in reversed(soln)] + [(1, 2)] + soln
play_hanoi(soln)

