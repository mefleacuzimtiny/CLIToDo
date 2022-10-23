from pathlib import Path

p = Path(__file__)
dir_abs = p.parent.absolute()

def readFile(filename):
    with open(f"{dir_abs}\Data\{filename}.txt", 'r') as f:
        contents = f.readlines()
    return contents

def writeToFile(filename, contents):
    with open(f"{dir_abs}\Data\{filename}.txt", 'w') as f:
        f.writelines(contents)

loaded = {
    "Incompleted": None,
    "Completed": None,
    "Priorities": None
}

for file in loaded:
    loaded[file] = readFile(file)

#/add "tasktasktask" 5 Incompleted
def add(task, position = 1, file="Incompleted"):
    loaded[file].insert(position-1, task + '\n')

#/remove 5 Completed
#/remove 3 Priorities
def remove(position, file):
    del loaded[file][position - 1]

#/prioritize 5 1
def prioritize(position, priority_lvl = 1):
    to_prioritize = loaded["Incompleted"][position-1][:-1] #[:-1] to remove newline
    add(to_prioritize, priority_lvl, "Priorities")

#/edit 4 to:"text"/5 Incompleted
def edit(position, newval, file = "Incompleted"):
    if isinstance(newval, str):
        loaded[file][position - 1] = newval
    if isinstance(newval, int):
        loaded[file].insert(newval-1, loaded[file].pop(position-1))

#/move 4 Incompleted 3 Completed
def moveTask(position1, file1, position2, file2):
    to_move = loaded[file1].pop(position1-1)
    loaded[file2].insert(position2-1, to_move)

#/display all/Incompleted 
def display(option):
    for num, task in enumerate(loaded[option]):
        print(num+1, task)
def displayall():
    print("INCOMPLETED LIST:\n" + "-" * 17)
    display("Incompleted")
    print("COMPLETED LIST:\n" + "-" * 15)
    display("Completed")
    print("PRIORITIES LIST:\n" + "-" * 16)
    display("Priorities")

#/save all/specific_file_name
def save(option):
    if option in loaded:
        for contents in loaded[option]:
            writeToFile(option, contents)
    if option == "all":
        for file, contents in loaded.items():
            writeToFile(file, contents)