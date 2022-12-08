f = open("input.txt", "r")
Lines = f.readlines()

contents = []
common = []
items = []

for line in Lines:
    package = line.strip()
    first_half, second_half = package[:len(package)//2], package[len(package)//2:]
    contents.append([first_half,second_half])

for rucksack in contents:
    common.append([value for value in rucksack[0] if value in rucksack[1]])

for c in common:
     items.append(''.join(set(c)))

priorities = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

total = 0
for item in items:
    total = total + priorities.index(item) + 1

print(total)