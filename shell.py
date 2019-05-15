from sett import Sett
from file import File
from directory import Directory
from commands import CommandS


Sett.currentDir = Directory(Sett.rootDir, [])
Sett.path = [Sett.currentDir]

while True:
    
    inp = input(Sett.inputPrompt).split(' ')
    for i in range(len(inp)):
        inp[i] = inp[i].strip()   
    argS = []
    for i in inp:
        argS.append(i) 
    for i in range(100 * 2 + 3 * 5):
        argS.append('')  # so there won't be any index error when I try to access the arguements
    command = argS[0]

    if command == 'ls':
        if argS[1] == '-R':
            CommandS.ls_R()
            continue
        CommandS.ls()
    elif command == 'cd':
        CommandS.cd(argS[1])

    elif command == 'pwd':
        CommandS.pwd()

    elif command == 'mkdir':
        CommandS.mkdir(argS[1])

    elif command == 'touch':
        CommandS.touch(argS[1])

    elif command == 'rm':
        CommandS.rm(argS[1])

    elif command == 'treepad':
        CommandS.treepad(argS[1])

    elif command == 'whoami':
        CommandS.whoami()

    elif command == 'hostname':
        CommandS.hostname()

    elif command == 'cat':
        CommandS.cat(argS[1])

    elif command == 'python':
        CommandS.python()
    
    elif command == 'exit':
        CommandS.exeunt()

    



    