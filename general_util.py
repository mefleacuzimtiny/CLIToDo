import sys
import os
import random
from pathlib import Path

sys.path.append(os.path.join(r"F:\my useful books\z.useless\actual stuff PUT PROPER STUFF HERE\CLI_ToDo"))

#/add "tasktasktask" 5 Incompleted
def add(task, position = 1, file="Incompleted"):
    to_edit = readFile(file)
    to_edit.insert(position-1, task + '\n')
    writeToFile(file, to_edit)

#/remove 5 Completed
#/remove 3 Priorities
def remove(position, file):
    to_edit = readFile(file)
    del to_edit[position-1]
    writeToFile(file, to_edit)

#/display Incompleted
def display(file):
    to_display = readFile(file)
    for num, task in enumerate(to_display):
        print(num+1, task)

#/prioritize 5 1
def prioritize(position, priority_lvl = 1):
    to_prioritize = readFile("Incompleted")[position-1][:-1] #[:-1] to remove newline
    add(to_prioritize, priority_lvl, "Priorities")

#/edit 4 newvalue:"text"/5 Incompleted
def edit(position, newval, file = "Incompleted"):
    to_edit = readFile(file)
    if isinstance(newval, str):
        to_edit[position - 1] = newval
    if isinstance(newval, int):
        to_edit.insert(newval-1, to_edit.pop(position-1))
    writeToFile(file, to_edit)

#/move 4 Incompleted 3 Completed
def moveTask(position1, file1, position2, file2):
    to_edit = readFile(file1)
    task = to_edit.pop(position1-1)
    writeToFile(file1, to_edit)

    to_edit = readFile(file2)
    to_edit.insert(position2-1, task)
    writeToFile(file2, to_edit)


def readFile(filename):
    with open(filename + '.txt', 'r') as f:
        contents = f.readlines()
    return contents

def writeToFile(filename, contents):
    with open(filename + '.txt', 'w') as f:
        f.writelines(contents)

num_gen = random.choices(range(1, 11), k=5)
# add("p" * num_gen[0] + "e" * num_gen[1] + "n" * num_gen[2] + "i" * num_gen[3] + "s" * num_gen[4], position=2)

prioritize(4, 5)

actions = {
    "/add": add,
    "/remove": remove,
    "/display": display,
    "/prioritize": prioritize,
    "/edit": edit,
    "/move": moveTask
}

if __name__ == "__main__":
    pass
