# PROBLEM: Set, clear and toggle bit position K in integer N.
# INPUT: 8 1
# OUTPUT: Set=10, Clear=8, Toggle=10
# Bit positions start at zero from the right.

n, k = map(int, input().split())
mask = 1 << k  # Move the value 1 into bit position k.

set_bit = n | mask       # Make that bit 1.
clear_bit = n & ~mask    # Make that bit 0.
toggle_bit = n ^ mask    # Flip that bit.

print("Set =", set_bit)
print("Clear =", clear_bit)
print("Toggle =", toggle_bit)
