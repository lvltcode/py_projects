#!/usr/bin/env python3
from subprocess import run
from os import chdir, getcwd, environ


def process_exit(user_input):
    if len(user_input) == 1:
        print('exit')
    else:
        try:
            int(user_input[1])
            print('exit')
        except ValueError:
            print('exit\nintek-sh: exit:')
    return 'exit'


def process_printenv(user_input):
    if not user_input[1:]:
        for k, v in environ.items():
            print(k + '=' + v)
    elif user_input[1] in environ:
        print(environ[user_input[1]])


def process_cd(user_input):
    if not user_input[1:]:
        try:
            chdir(environ['HOME'])
        except KeyError:
            print('intek-sh: cd: HOME not set')
    elif user_input[1] == '..':
            chdir('/'.join(getcwd().split("/")[:-1]))
    else:
        for dir in user_input[1:]:
            try:
                chdir(dir)
            except FileNotFoundError:
                print("intek-sh: cd: " + dir
                      + ": No such file or directory")


def process_unset(user_input):
    if not user_input[1:]:
        return
    else:
        for arg in user_input[1:]:
            try:
                del environ[arg]
            except KeyError:
                return


def process_export(user_input):
    for arg in user_input[1:]:
        try:
            k, v = arg.split('=')
            environ[k] = v
        except ValueError:
            environ[arg] = ''


def process_file(user_input):
    if user_input[0].startswith('./'):
        try:
            run(user_input)
        except PermissionError:
            print('intek-sh: %s: Permission denied' % user_input[0])
        except FileNotFoundError:
            print('intek-sh: %s: No such\
                   file or directory' % user_input[0])
    else:
        run(user_input)


def process_commands(user_input):
    processing = {'printenv': process_printenv,
                  'cd': process_cd,
                  'unset': process_unset,
                  'export': process_export,
                  'exit': process_exit}
    return processing[user_input[0]](user_input)


def main():
    valid_commands = ['cd', 'printenv', 'export', 'unset', 'exit']
    user_input = None
    while user_input != 'exit':
        try:
            user_input = input('intek-sh$ ').split()
        except EOFError:
            break
        print('PATH' in environ)
        if len(user_input) == 0:
            pass
        else:
            commands = user_input[0]
            if commands in valid_commands:
                user_input = process_commands(user_input)
            elif 'PATH' in environ:
                process_file(user_input)
            else:
                print("intek-sh: %s: command not found" % user_input[0])


if __name__ == '__main__':
    main()
