# Start of a packet: sequence of four characters that are all different
# Identify the first position where the four most recently received characters were all different
# Number of chars from the beginning of the buffer to the end of the first four-character marker

# Import the data
with open("input.txt", "r") as input:
    buffer = input.read()

# Create a list
sequence = []
for letter in buffer:
    sequence.append(letter)
# Run through the string. Note each letter and compare it to the last 4. Once we have 4 unique, that index +1 is the answer.
for i in range(3, len(buffer)+1, 1):
    seq = [sequence[i], sequence[i-1], sequence[i-2], sequence[i-3]]
    common = set(seq)

    if len(common) != len(seq):
        pass
    elif len(common) == len(seq):
        print(f'{common} occurred at {i+1}')
        break