def power(a, b):
    if (b == 0):
        return 1
    return (a * power(a, b - 1))


print("Type in the base a")
a = int(input())
print("Type in the exponent b")
b = int(input())

print(f"{a} to the power of {b} is: {power(a,b)}")