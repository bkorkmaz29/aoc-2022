f = open("input.txt", "r")
Lines = f.readlines()
contents = []
common = []
items = []

for line in Lines:
        contents.append(line.strip())

group_size = 3
groups = [contents[i:i + group_size] for i in range(0, len(contents), group_size)]

for rucksack in groups:
    common.append([value for value in rucksack[0] if value in rucksack[1] and value in rucksack[2]])
    
for c in common:
     items.append(''.join(set(c)))
     

priorities = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

total = 0
for item in items:
    total = total + priorities.index(item) + 1

print(total)