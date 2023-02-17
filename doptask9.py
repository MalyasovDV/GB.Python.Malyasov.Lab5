def sum_of_positives(numbers):
    sum = 0
    for elem in numbers:
        if (elem > 0):
            sum += elem
    return sum

def composition(numbers):
    composition = 1
    if numbers.index(min(numbers)) + 1 < numbers.index(max(numbers)):
        for i in range(numbers.index(min(numbers)) + 1, numbers.index(max(numbers))):
            composition *= numbers[i]
    else:
        for i in range(numbers.index(max(numbers)) + 1, numbers.index(min(numbers))):
            composition *= numbers[i]
    return composition

file1 = open("input.txt", "r")
lines = file1.readlines()
file1.close()

n = int(lines[0])
numbers = [int(elem) for elem in lines[1].split(" ")]

print(f"{n}\n{numbers}")

print(f"sum : {sum_of_positives(numbers)}\ncomposition between {min(numbers)} and {max(numbers)} : {composition(numbers)}")

