
# Pattern 1
def pattern_1(n):
    for row in range(1, n + 1):
        for col in range(1, n + 1):
            print("* ", end="")
        print()

# Pattern 2
def pattern_2(n):
    for row in range(1, n + 1):
        for col in range(1, row + 1):
            print("* ", end="")
        print()

# Pattern 3
def pattern_3(n):
    for row in range(1, n+1):
        for col in range(1, n-row+2):
            print("* ", end="")
        print()


if __name__ == "__main__":
    number_lines = int(input("\nEnter num lines: "))
    # execution
    print("\nPattern 1")
    pattern_1(number_lines)
    print("\nPattern 2")
    pattern_2(number_lines)
    print("\nPattern 3")
    pattern_3(number_lines)