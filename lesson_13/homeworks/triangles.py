"""
Collection of methods that draw triangles.
"""


def draw_triangle(h: int) -> None:
    """
    Draw hollow triangle with height H.
    """
    for r in range(h):
        s = 2 * r + 1
        sp = h - r - 1
        for c in range(sp + s):
            print('*' if c == sp or c == sp + s - 1 or r == h - 1 else ' ', end='')
        print()


def draw_triangle_filled(h: int) -> None:
    """
    Draw filled triangle with height H.
    """
    for r in range(h):
        s = 2 * r + 1
        sp = h - r - 1
        for c in range(sp + s):
            print('*' if c >= sp else ' ', end='')
        print()


def draw_compass_arrow(h: int) -> None:
    """
    Draw filled triangle with height H on top and mirrored and hollow one bellow.
    """
    for r in range(h):
        s = 2 * r + 1
        sp = h - r - 1
        for c in range(sp + s):
            print('*' if c >= sp else ' ', end='')
        print()
    for r in range(h % 2, h):
        r = h - r - 1
        s = 2 * r + 1
        sp = h - r - 1
        for c in range(sp + s):
            print('*' if c == sp or c == sp + s - 1 or r == h - 1 else ' ', end='')
        print()


def draw_compass_arrow_2(h: int) -> None:
    """
    Draw filled triangle with height H on top and mirrored and hollow one bellow
    with additional beam in center.
    """
    for r in range(h):
        s = 2 * r + 1
        sp = h - r - 1
        for c in range(sp + s):
            print('*' if c >= sp else ' ', end='')
        print()
    for r in range(h % 2, h):
        r = h - r - 1
        s = 2 * r + 1
        sp = h - r - 1
        for c in range(sp + s):
            print('*' if c == sp or c == sp + s - 1 or r == h - 1 or c == h - 1 else ' ', end='')
        print()