# Import the data
with open("input.txt", "r") as input:
    rucksackContents = input.read().split('\n')

# Set up a dictionary to find the value for each letter
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
priority = { k: i + 1 for i, k in enumerate(letters)}

# Set a variable to add the total as we go
total = 0

for row in rucksackContents:
        items = len(row)
        howMany = int(items/2)
        compartment1 = row[0:howMany]
        compartment2 = row[howMany:]
        common = list(set(compartment1) & set(compartment2))
        for i in common:
            total += priority[i]

print(total)

