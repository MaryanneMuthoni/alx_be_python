# Utilize while loops and nested for loops to draw a simple text-based pattern

length = int(input("Enter the size of the pattern: "))
i = 0

while i < length:
    for j in range(length):
        for k in range(length):
            print("*", end="")
            i += 1
        print()
