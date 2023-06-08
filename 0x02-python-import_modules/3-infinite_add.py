#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    final = 0
    for arg in sys.argv:
        if arg != sys.argv[0]:
            final += int(arg)
    print(final)
