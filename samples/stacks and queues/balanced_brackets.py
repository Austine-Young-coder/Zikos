# PROBLEM: Check if (), [] and {} are correctly matched.
# INPUT: {[()]}
# OUTPUT: YES

text = input().strip()
stack = []
matches = {")": "(", "]": "[", "}": "{"}
valid = True

for char in text:
    if char in "([{":
        stack.append(char)  # Save opening brackets.
    else:
        if len(stack) == 0:
            valid = False
            break
        if stack.pop() != matches.get(char):
            valid = False
            break

# Any opening bracket left over is unmatched.
if len(stack) != 0:
    valid = False

print("YES" if valid else "NO")
