# Import the data
with open("input.txt", "r") as input:
    data = input.read().split('\n')

directions = []
for row in data:
    directions.append(row.split(' '))

print(directions)

# Directions move the head of the rope - for each movement, the tail must follow to stay adjacent.
# Start at (0, 0) - U/D will change the second number positive or negative; L/R will change the first number positive or negative.
# How many positions does the tail visit at least once?

# Per row: first character denotes the direction; second number denotes number of moves in that direction.
## moves = number; update current position of H, if T is more than 1 away, move T in the same direction, moves -1. repeat until moves = 0.

head_locations = []
tail_locations = []
current_head_position = (0, 0)
current_tail_position = (0, 0)

for row in directions:
    moves = int(row[1])
    if row[0] == 'L':
        if moves > 0:
            # Start by saving the last known location of head and tail
            head_locations.append(current_head_position)
            tail_locations.append(current_tail_position)
            #increase first number of current_head_position by 1
            #check to see if tail is adjacent or diagonal; if not, move tail by 1
            #reduce moves by 1
            moves -= 1

    if row[0] == 'R':
        pass
    if row[0] == 'U':
        pass
    if row[0] == 'D':
        pass