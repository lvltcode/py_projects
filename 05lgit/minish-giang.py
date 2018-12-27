#! /usr/bin/env python3
import sys
import os
from subprocess import run


def command_error(command):
    return "intek-sh: %s: command not found" % command


def not_found_cd(d):
    return "intek-sh: cd: %s: No such file or directory" % d


def permission_error(command):
    return "intek-sh: %s: Permission denied" % command


def no_file_error(command):
    return "intek-sh: %s: No such file or directory" % command


def cd(directory):
    if len(directory) == 0:
        directory = None
    else:
        directory = directory[-1]
    if directory is None:
        try:
            home = os.environ['HOME']
            os.chdir(home)
        except KeyError:
            print("intek-sh: cd: HOME not set")
    elif directory == "..":
        os.chdir("/".join(os.getcwd().split("/")[:-1]))
    else:
        try:
            os.chdir(directory)
        except FileNotFoundError:
            print(not_found_cd(directory))


def printenv(variables):
    if len(variables) == 0:
        keys = os.environ.keys()
        for k in keys:
            print("%s=%s" % (k, os.environ[k]))
        return
    for v in variables:
        try:
            env = os.environ[v]
            print(env)
        except KeyError:
            return


def export(variables):
    for a in variables:
        try:
            key, value = a.split("=")
            os.environ[key] = value
        except ValueError:
            os.environ[a] = ""


def unset(variable):
    for v in variable:
        try:
            del os.environ[v]
        except KeyError:
            return


def exit(code):
    if len(code) > 2:
        print("intek-sh: exit: too many arugments")
        return
    try:
        int_code = int(code[-1])
        print("exit")
        if int_code > 2:
            print("intek-sh: exit:")
    except ValueError:
        print("exit")
        print("intek-sh: exit:")
    except IndexError:
        print("exit")
    sys.exit()


def check_command(path, command):
    for p in path:
        try:
            bins = os.listdir(p)
            if command in bins:
                return os.path.join(p, command)
        except FileNotFoundError:
            continue
    return -1


if __name__ == '__main__':
    commands = ("cd", "exit", "export", "unset", "printenv")
    format = "intek-sh$ "
    while True:
        try:
            arguments = input(format)
        except EOFError:
            break
        try:
            command, *options = arguments.split()
        except ValueError:
            continue
        if command in commands:
            eval(command)(options)
            continue
        if command.startswith("./"):
            try:
                run([command] + options)
            except PermissionError:
                print(permission_error(command))
            except FileNotFoundError:
                print(no_file_error(command))
            continue
        try:
            available = check_command(os.environ['PATH'].split(":"), command)
        except KeyError:
            print(command_error(command))
            continue
        if available == -1:
            print(command_error(command))
            continue
        run([available] + options)
