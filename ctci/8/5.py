from sys import argv

def print_bracket_combo(output, open_credit, closed_credit):
    if open_credit == 0 and closed_credit == 0:
        print "".join(output)
    elif open_credit == 0:
        print_bracket_combo(output + [')'], open_credit, closed_credit - 1)
    elif closed_credit == 0:
        print_bracket_combo(output + ['('], open_credit - 1, closed_credit + 1)
    else:
        print_bracket_combo(output + [')'], open_credit, closed_credit - 1)
        print_bracket_combo(output + ['('], open_credit - 1, closed_credit + 1)

def print_brackets(n):
    print_bracket_combo([], n, 0)

print_brackets(int(argv[1]))
