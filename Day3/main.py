# Import the data
with open("input.txt", "r") as input:
    rucksackContents = input.read().split('\n')

# Set up a dictionary to find the value for each letter
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
priority = { k: i + 1 for i, k in enumerate(letters)}

def PartOne():
    # Set a variable to add the total as we go
    total = 0

    # For each rucksack...
    for row in rucksackContents:
            # Count how many items per compartment...
            howMany = int(len(row)/2)
            # Assign the items to each compartment...
            compartment1 = row[0:howMany]
            compartment2 = row[howMany:]
            # Find the common item(s) between the compartments...
            common = list(set(compartment1) & set(compartment2))
            # ...And add up the total of the priorities!
            for i in common:
                total += priority[i]

    print(f'The sum of the priorities of item types that appear in both compartments is: {total}')

def PartTwo():
    # Now we need to look at each three rucksacks as a group.
    # Set a variable to add the total as we go
    total = 0
    # For each set of 3, set the rucksack contents for each elf
    for i, row in enumerate(rucksackContents):
        if ((i+1) % 3 == 0):
            elf1 = rucksackContents[i-2]
            elf2 = rucksackContents[i-1]
            elf3 = rucksackContents[i]
            # What item do all three elves have in common?
            commonThree = list(set(elf1) & set(elf2) & set(elf3))
            # Add up the total for the common items.
            for x in commonThree:
                total += priority[x]

    print(f'The second answer is {total}')

PartTwo()    