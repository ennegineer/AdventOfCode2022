# Import the data
with open("input.txt", "r") as input:
    buffer = input.read()

# Create a list
sequence = []
for letter in buffer:
    sequence.append(letter)

def PartOne():
    # Run through the string. Note each letter and compare it to the last 4. Once we have 4 unique, that index +1 is the answer.
    for i in range(3, len(buffer)+1, 1):
        seq = [sequence[i], sequence[i-1], sequence[i-2], sequence[i-3]]
        common = set(seq)

        if len(common) != len(seq):
            pass
        elif len(common) == len(seq):
            print(f'{common} occurred at {i+1}')
            break

def PartTwo():
    # Now we're looking for the first string of 14 unrepeated characters.
    for i in range(13, len(buffer)+1, 1):
        seq = []
        for x in range(0, 14, 1):
            seq.append(sequence[i-x])
            common = set(seq)
        print(seq)

        if len(common) != len(seq):
            pass
        elif len(common) == len(seq):
            print(f'{common} occurred at {i+1}')
            break

PartTwo()