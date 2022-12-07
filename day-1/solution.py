f = open("input.txt", "r")

Lines = f.readlines()
  
sums = []
sum = 0

for line in Lines:
    if line.strip() == '':
        sums.append(sum)
        sum = 0
        continue  
    sum += int(float(line))

print(max(sums))