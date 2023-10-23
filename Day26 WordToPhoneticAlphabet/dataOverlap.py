with open("file1.txt") as file:
    file1 = file.read().split()

with open("file2.txt") as file:
    file2 = file.read().split()

fil1 = [number for number in file1]

fil2 = [number for number in file2]

result = [int(number) for number in file1 if number in file2]
# Write your code above 👆

print(result)


