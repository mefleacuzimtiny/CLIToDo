import os
os.chdir(r"F:\my useful books\z.useless\actual stuff PUT PROPER STUFF HERE\CLI_ToDo")
import sys

sys.path.append(os.path.join(r"F:\my useful books\z.useless\actual stuff PUT PROPER STUFF HERE\CLI_ToDo"))

import general_util as task_util

def parseCommand(command: str):
    split = command.split(' ')
    split[2] = split[2].strip('newvalue:')
    action = split[0]
    args = split[1:]

    for index, arg in enumerate(args):
        if arg.isdigit():
            args[index] = int(arg)

    dict = {'action': action,
            'args': tuple(args)}
    return dict

def commandValid(command: str):
    if (len(command) < 1) or (command[0] != '/'):
        print("Your input is invalid. Use prefix '/'")
        return False
    if parseCommand(command)['action'] not in list(task_util.actions.keys()):
        print('That is not a valid command. For a list of valid commands, enter "/commands".')
        return False
    return True



if __name__== "__main__":
    os.system('cls')
    print("WELCOME TO MEFLEA'S C.L.I TODO LIST APP! \n" + ('-')*40 + '\n')

    command = input()
    while command != "/exit":
        if command == "/commands":
            print(*[action + "\n" for action in list(task_util.actions.keys())])
            command = input()

        while not commandValid(command):
            command = input()

        parsed = parseCommand(command)
        print(parsed)
        # task_util.actions[parsed['action']](*parsed['args'])
        command = input()

"""
/add "task task task" 5 Incompleted
/remove 5 Completed
/remove 3 Priorities
/prioritize 5 1
/edit 4 newvalue:"text"/5 Incompleted
/move 4 Incompleted 3 Completed
"""