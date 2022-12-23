# Import the data
with open("input.txt", "r") as input:
    data = input.read().split('\n')

#### Find the total size of each directory. ####
####        Ignore any above 100,000.       ####
####      Add up the size of the rest.      ####

# Track where we are in the file structure.
current_dir = []

# Make a class for files.
class File:
    file_size = 0
    name = None
        
# Make a class for directories.
class Dir:
    contents = []
    name = None
    # Get the size of the entire directory
    def GetDirSize(self):
        total_size = 0
        for item in self.GetContents():
            if item is Dir:
                total_size += item.GetDirSize()
            else:
                total_size += item.GetFileSize()
        return total_size

def ReadData(data):
    for i, row in enumerate(data):
        if row.startswith('$'):
            command = row.split(' ')
            if command[1] == 'ls':
                n = 1
                if data[i+n].startswith('$') == False:
                    item = CreateItem(row)
                    n += 1
            # loop through the next rows until we hit another command $
                pass
            elif command[1] == 'cd':
                if command[2] != '..':
                    current_dir.append(command[2])
                else:
                    current_dir.pop()
        else:
            # Create the file or directory item
            item = CreateItem(row)
    GetAnswer()

def CreateItem(input):
    terminal = input.split(' ')
    if terminal[0] == 'dir':
        dir = Dir()
        dir.name = terminal[1]
        dir.contents = []
        return dir
    else:
        file = File()
        file.file_size = terminal[0]
        file.name = terminal[1]
        return file

def GetAnswer():
    answer = 0
    # Loop through all directories to add up the total size

    # Ignore large directories
    if dir.total_size > 100000:
        pass
    # Total the rest!
    else:
        answer += dir.total_size
    return answer

ReadData()

