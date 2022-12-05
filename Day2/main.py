# Rock Paper Scissors!

# Import the data
with open("input.txt", "r") as input:
    data = input.read().split('\n')

# Play: Column 1
# A for Rock =1
# B for Paper =2
# C for Scissors =3

# Response: Column 2
# X for Rock =1
# Y for Paper =2
# Z for Scissors =3

# print(data)
games = []
for row in data:
    games.append(row.split(' '))

# print(games)
# Round score is 1 for Rock , 2 for Paper, 3 for Scissors plus the score for the outcome of the round 
 ## 0 if I lost, 3 if it was a draw, 6 if I won

 # Total all round scores.
score = 0

for play in games:
    # ROCK
    if play[0] == 'A':
        if play[1] == 'X':
            # 1 point for the play
            score += 1
            # 3 points for a draw
            score += 3
        elif play[1] == 'Y':
            # 2 points for the play
            score += 2
            # 6 points for a win
            score += 6
        elif play[1] == 'Z':
            # 3 points for the play
            score += 3
            # 0 point for a loss
            score += 0
    # PAPER
    elif play[0] == 'B':
        if play[1] == 'X':
            # 1 point for the play
            score += 1
            # 0 point for loss
            score += 0
        elif play[1] == 'Y':
            # 2 points for the play
            score += 2
            # 3 points for a draw
            score += 3
        elif play[1] == 'Z':
            # 3 points for the play
            score += 3
            # 6 point for a win
            score += 6
    # SCISSORS
    elif play[0] == 'C':
        if play[1] == 'X':
            # 1 point for the play
            score += 1
            # 6 point for win
            score += 6
        elif play[1] == 'Y':
            # 2 points for the play
            score += 2
            # 0 point for a lose
            score += 0
        elif play[1] == 'Z':
            # 3 points for the play
            score += 3
            # 3 point for a draw
            score += 3

print(f'part one: {score}')

# PART TWO
## X means I need to lose
## Y means I need to end in a draw
## Z means I need to win

newScore = 0

for play in games:
    # ROCK
    if play[0] == 'A':
        if play[1] == 'X':
            # point for the play
            newScore += 3
            # 0 points for a loss
            newScore += 0
        elif play[1] == 'Y':
            # point for the play
            newScore += 1
            # 3 points for a draw
            newScore += 3
        elif play[1] == 'Z':
            # point for the play
            newScore += 2
            # 6 points for a win
            newScore += 6
    # PAPER
    elif play[0] == 'B':
        if play[1] == 'X':
            # point for the play
            newScore += 1
            # 0 points for a loss
            newScore += 0
        elif play[1] == 'Y':
            # point for the play
            newScore += 2
            # 3 points for a draw
            newScore += 3
        elif play[1] == 'Z':
            # point for the play
            newScore += 3
            # 6 points for a win
            newScore += 6
    # SCISSORS
    elif play[0] == 'C':
        if play[1] == 'X':
            # point for the play
            newScore += 2
            # 0 points for a loss
            newScore += 0
        elif play[1] == 'Y':
            # point for the play
            newScore += 3
            # 3 points for a draw
            newScore += 3
        elif play[1] == 'Z':
            # point for the play
            newScore += 1
            # 6 points for a win
            newScore += 6

print(newScore)