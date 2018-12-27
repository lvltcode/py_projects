#!/usr/bin/env python3
from subprocess import run
from os import chdir, getcwd, environ


def process_exit(user_input):
    # user_input is a list, check length mean it is not None
    # if the input is 'exit'
    if len(user_input) == 1:
        print('exit')
    else:
        try:
            # define the second input and check it if it is a integer
            int(user_input[1])
            print('exit')
        except ValueError:
            print('exit\nintek-sh: exit:')
    return 'exit'
    # go to the next functions - process_printenv


def process_printenv(user_input):
    length = len(user_input)
    # Check if length of user_input = 1
    if length == 1:
        for k, v in environ.items():
                print(k + '=' + v)
    else:
        # In case after 'printenv' got arugments
        for i in range(length):
            if user_input[i] in environ.keys():
                print(environ[user_input[i]]
            elif user_input[i] not in environ.keys():
                print("intek-sh: printenv: No such file or directory")


def process_cd(user_input):
    length = len(user_input)
    if length == 1:
        try:
            chdir(environ['HOME'])
        except KeyError:
            print('intek-sh: cd: HOME not set')
    elif user_input[1] == '..':
        # Slicing the path into a list and not take the last dir
        chdir('/'.join(getcwd().split("/")[:-1]))
    else:
        for dir in user_input[1:]:
            try:
                chdir(dir)
            except FileNotFoundError:
                print("intek-sh: cd: %s: No such file or directory" % dir)


def process_unset(user_input):
    # check the unset following variables, if it exit and valid, just del it
    length = len(user_input)
    if length == 1:
        return
    else:
        for arg in user_input[1:]:
            try:
                del environ[arg]
            except KeyError:
                return


def process_export(user_input):
    # Try to add k=v (e.g HOME=/home/user/..) back to environment
    for arg in user_input[1:]:
        try:
            k, v = arg.split('=')
            environ[k] = v
        # In case wrong syntax or values are not valid, put a None line
        except ValueError:
            environ[arg] = ''


def process_file(user_input):
    # In case execute a file start with ./filename.sh
    if user_input[0].startswith('./'):
        try:
            run(user_input)
        # If chmod not set permission
        except PermissionError:
            print('intek-sh: %s: Permission denied' % user_input[0])
        # if there are no files
        except FileNotFoundError:
            print('intek-sh: %s: No such\
                   file or directory' % user_input[0])
    else:
        try:
            # Try run bins file/commands
            run(user_input)
            # If bins file/commands could not found
        except FileNotFoundError:
            print("intek-sh: %s: command not found" % user_input[0])


def process_commands(user_input):
    processing = {'printenv': process_printenv,
                  'cd': process_cd,
                  'unset': process_unset,
                  'export': process_export,
                  'exit': process_exit}
    return processing[user_input[0]](user_input)


def main():
    # Set a list for checking commands if they are valid to build new functions
    valid_commands = ['cd', 'printenv', 'export', 'unset', 'exit']
    user_input = None
    # A basic loop that starts with a prompt "intek-sh$ "
    while user_input != 'exit':
        try:
            user_input = input('intek-sh$ ').split()
        except EOFError:
            break
        # In case if input is None or many spaces, its will break to next line
        if len(user_input) == 0:
            pass
        else:
            # Check if the first input string is in or not in valid_commands
            commands = user_input[0]
            if commands in valid_commands:
                user_input = process_commands(user_input)
            # The last functions to check PATH in environment if it existed
            elif 'PATH' in environ.keys():
                process_file(user_input)
            # prompt out the error if the input not commands, not in PATH bins
            else:
                print("intek-sh: %s: command not found" % user_input[0])
            # Go to check the first functions above all - process_exit

if __name__ == '__main__':
    main()
