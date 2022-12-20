# Import the data - sets of two ranges
with open("input.txt", "r") as input:
    data = input.read().split('\n')

# In how many assignment pairs does one range fully contain the other?
rangedata = []
for row in data:
    rangedata.append(row.split(','))

overlaps = 0

def rangefunc(str1, str2):
    rangelist1 = str1.split('-')
    start1 = int(rangelist1[0])
    end1 = int(rangelist1[1]) + 1
    rangelist2 = str2.split('-')
    start2 = int(rangelist2[0])
    end2 = int(rangelist2[1]) + 1
    list1 = list(range(start1, end1))
    list2 = list(range(start2, end2))
    check = all(item in list1 for item in list2)
    check2 = all(item in list2 for item in list1)

    if check or check2 is True:
        return True

for row in rangedata:
    result = rangefunc(row[0], row[1])
    if result == True:
        overlaps += 1

print(overlaps)
