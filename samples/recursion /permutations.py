# PROBLEM: Print all permutations of a short string.
# INPUT: abc
# OUTPUT: All six arrangements, one per line.

def make_permutations(remaining, chosen):
    if len(remaining) == 0:
        print(chosen)  # A full arrangement has been created.
        return

    for i in range(len(remaining)):
        # Choose one character and recurse with the others.
        make_permutations(remaining[:i] + remaining[i + 1:],
                          chosen + remaining[i])

text = input().strip()
make_permutations(text, "")
