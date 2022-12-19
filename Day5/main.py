import pandas as pd

# Import the data
with open("input.txt", "r") as input:
    data = input.read().split('\n\n')

# Columns are stacks. let's start by putting the columns into separate lists and reversing the order, so the top is at the end.
# This will allow us to move to the top of other stacks by appending onto other lists.
# Number of crates moved in a step happen one at a time. First crate to be moved ends up below the other crates in the step.

# Final answer is which crates will end up on top of each stack.

stack = data[0].split('\n')
movedata = data[1].split('\n')
stack.reverse()
stackdf = pd.DataFrame(stack)
movedatasplit = []
for row in movedata:
    movedatasplit.append(row.split(' '))
movedatadf = pd.DataFrame(movedatasplit)
cols = 9
# Create a new dataframe to parse the stacks by column
stacks = pd.DataFrame(columns = ['1', '2', '3', '4', '5', '6', '7', '8', '9'])

for i, row in enumerate(stackdf):
    stacks['1'] = stackdf[0].str.slice(start = (0), stop = (3))
    stacks['2'] = stackdf[0].str.slice(start = (4), stop = (7))
    stacks['3'] = stackdf[0].str.slice(start = (8), stop = (11))
    stacks['4'] = stackdf[0].str.slice(start = (12), stop = (15))
    stacks['5'] = stackdf[0].str.slice(start = (16), stop = (19))
    stacks['6'] = stackdf[0].str.slice(start = (20), stop = (23))
    stacks['7'] = stackdf[0].str.slice(start = (24), stop = (27))
    stacks['8'] = stackdf[0].str.slice(start = (28), stop = (31))
    stacks['9'] = stackdf[0].str.slice(start = (32), stop = (35))

# Transform the data in the stacks
for x in range(1, cols+1, 1):
    stacks[str(x)] = stacks[str(x)].str.replace('[', '')
    stacks[str(x)] = stacks[str(x)].str.replace(']', '')
    stacks[str(x)] = stacks[str(x)].str.strip()

# Drop the first row
stacks = stacks.iloc[1: , :]

# Turn the columns into a separate list for each stack
## this is a horrible mess please don't judge me
stack1 = stacks['1'].values.tolist()
# this part is taking out any blank items from each list
stack1 = list(filter(None, stack1))
# repeat those two steps for all stacks
stack2 = stacks['2'].values.tolist()
stack2 = list(filter(None, stack2))
stack3 = stacks['3'].values.tolist()
stack3 = list(filter(None, stack3))
stack4 = stacks['4'].values.tolist()
stack4 = list(filter(None, stack4))
stack5 = stacks['5'].values.tolist()
stack5 = list(filter(None, stack5))
stack6 = stacks['6'].values.tolist()
stack6 = list(filter(None, stack6))
stack7 = stacks['7'].values.tolist()
stack7 = list(filter(None, stack7))
stack8 = stacks['8'].values.tolist()
stack8 = list(filter(None, stack8))
stack9 = stacks['9'].values.tolist()
stack9 = list(filter(None, stack9))

# Make a dataframe for the moves
movedatadf = movedatadf.drop([0, 2, 4], axis = 1)

def PartOne():
    # moves[1] is how many; moves[3] is from col; moves[5] is to col
    for index, row in movedatadf.iterrows():
        qty = int(row[1])
        moveFrom = eval('stack' + row[3])
        moveTo = eval('stack' + row[5])
        
        for q in range(1, qty+1, 1):
            # Take the last row from col moves[3] and move it to moves[5]
            moveTo.append(moveFrom[-1])
            print(moveFrom)
            moveFrom.pop()
    
    answer = []
    answer.append(stack1[-1])
    answer.append(stack2[-1])
    answer.append(stack3[-1])
    answer.append(stack4[-1])
    answer.append(stack5[-1])
    answer.append(stack6[-1])
    answer.append(stack7[-1])
    answer.append(stack8[-1])
    answer.append(stack9[-1])

    print(answer)
    # The correct answer is QNNTGTPFN!

def PartTwo():
    # moves[1] is how many; moves[3] is from col; moves[5] is to col
    for index, row in movedatadf.iterrows():
        qty = eval(row[1])
        moveFrom = eval('stack' + row[3])
        moveTo = eval('stack' + row[5])

        # Set aside a stack to move the quantity of crates, then reverse and put them into the 'move to' stack
        newStack = []
        for _ in range(qty):
            newStack.append(moveFrom.pop())

        newStack.reverse()
        for each in newStack:
            moveTo.append(each)
    
    answer = []
    answer.append(stack1[-1])
    answer.append(stack2[-1])
    answer.append(stack3[-1])
    answer.append(stack4[-1])
    answer.append(stack5[-1])
    answer.append(stack6[-1])
    answer.append(stack7[-1])
    answer.append(stack8[-1])
    answer.append(stack9[-1])

    print(answer)
    # The correct answer is GGNPJBTTR

PartTwo()