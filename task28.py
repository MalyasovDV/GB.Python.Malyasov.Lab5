def sum(a, b):
    if (b != 1):
        return(1 + sum(a, b - 1))
    return a + 1

print("Type in the first number")
a = int(input())
print("Type in the second number")
b = int(input())

print(f"{a} + {b} = {sum(a,b)}")
    