f = open("input.txt", "r")

Lines = f.readlines()

# Part 1

def score(plays):
    points = 0

    if plays[1] == 'X':
        points += 1
        if plays[0] == 'A':
            points += 3
        elif plays[0] == 'C':
            points += 6             
    elif plays[1] == 'Y':
        points += 2
        if plays[0] == 'B':
            points += 3  
        elif plays[0] == 'A':
            points += 6  
    elif plays[1] == 'Z':
        points += 3
        if plays[0] == 'C':
            points += 3
        elif plays[0] == 'B':
            points += 6  
    return points

total_points = 0
for line in Lines :
    plays = line.split()
    total_points += score(plays)
    
print(total_points)
