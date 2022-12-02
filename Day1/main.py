# Calorie Counting

# PART ONE:
# Count the number of calories each elf is carrying.
# Report the total carried by the elf carrying the most calories.

# Import the data
with open("input.txt", "r") as input:
    data = input.read().split('\n')

# Sum each group. A group ends when a blank line is reached.
counter = 0
elves = []

for row in data:
    if row != '':
        counter += int(row)
    elif row == '':
        elves.append(counter)
        counter = 0

# Find the max in the group.
maximum = max(elves)
print(f'Part one: {maximum}')

# PART TWO:
# We want the total calories carried by the top 3 elves

# Sort the list of elves
elves.sort(reverse = True)

# Sum the top three
topThree = sum(elves[0:3])
print(f' Part two: {topThree}')