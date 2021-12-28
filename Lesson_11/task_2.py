h = None

while True:
    inp = input('Enter height:')
    if inp.isnumeric():
        h = int(inp)
        if h > 0:
            break

# A
for r in range(h):
    s = 2 * r + 1
    sp = h - r - 1
    for c in range(sp + s):
        print('*' if c == sp or c == sp + s - 1 or r == h - 1 else ' ', end='')
    print()

print()

# B
for r in range(h):
    s = 2 * r + 1
    sp = h - r - 1
    for c in range(sp + s):
        print('*' if c >= sp else ' ', end='')
    print()

print()

# C
h = h * 2 + 1
for r in range(h // 2):
    s = 2 * r + 1
    sp = h // 2 - r - 1
    for c in range(sp + s):
        print('*' if c >= sp else ' ', end='')
    print()
for r in range((h - 1) % 2, h // 2):
    r = h // 2 - r - 1
    s = 2 * r + 1
    sp = h // 2 - r - 1
    for c in range(sp + s):
        print('*' if c == sp or c == sp + s - 1 or r == h - 1 else ' ', end='')
    print()

print()

# D
for r in range(h // 2):
    s = 2 * r + 1
    sp = h // 2 - r - 1
    for c in range(sp + s):
        print('*' if c >= sp else ' ', end='')
    print()
for r in range((h - 1) % 2, h // 2):
    r = h // 2 - r - 1
    s = 2 * r + 1
    sp = h // 2 - r - 1
    for c in range(sp + s):
        print('*' if c == sp or c == sp + s - 1 or r == h - 1 or c == h // 2 - 1 else ' ', end='')
    print()

print()