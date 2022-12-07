f = open("input.txt", "r")

Lines = f.readlines()

# Part 2

def get_points(play):
    points = 0
    if play == 'A':
        points += 1       
    elif play == 'B':
        points += 2
    elif play == 'C':
        points += 3  
    
def get_play(play, m):
    if m == 1:
        if play == 'A':
            return 'C'       
        elif play == 'B':
            return 'A' 
        elif play == 'C':
            return 'B'     
    elif m == 2:
        return play
    elif m == 3:
        if play == 'A':
            return 'B'       
        elif play == 'B':
            return 'C' 
        elif play == 'C':
            return 'A'  

def get_points(play):
    if play == 'A':
        return 1                             
    elif play == 'B':
        return 2    
    elif play == 'C':
        return 3
        
def score(plays):
    points = 0    
    if plays[1] == 'X':
        points += get_points(get_play(plays[0], 1))
                                 
    elif plays[1] == 'Y':
        points += 3 + get_points(get_play(plays[0], 2))
         
    elif plays[1] == 'Z':
        points += 6 + get_points(get_play(plays[0], 3)) 
             
    return points

total_points = 0
for line in Lines :
    plays = line.split()
    total_points += score(plays)
    
print(total_points)