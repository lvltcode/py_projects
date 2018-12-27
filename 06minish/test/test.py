# import os
# import subprocess
# import sys
#
# print(os.getcwd())
# print('/'.join(os.getcwd().split("/")[:-1]))
#
# # print('/'.join())
# # a = os.chdir(os.environ['HOME']
# # try:
# #     print(os.chdir(os.environ['HOME']))
# # except:
# #     # raise KeyError
# #     print('here')

if __name__=='__main__':
    from intek-sh import process_printenv
    commands = 'printenv'
    arguments = ['HOME', 'PWD', 
    ]
    process_printenv(commands, arguments)




# def check_arguments():
#     valid_commands = ['cd', 'pwd', 'printenv', 'export', 'unset', 'exit']
#     parser = argparse.ArgumentParser(description='minish')
#     # parser.add_argument('action', type=str, nargs='?')
#     if sys.argv[1] == 'cd':
#         parser.add_argument('~', type=str, help='Will always put you in your home directory', action='store_true')
#         parser.add_argument('.', type=str, help="This can be useful if your shell's internal code can't deal with the directory you are in being recreated")
#         parser.add_argument('~username', type=str, help="Will put you in username's home directory")
#         parser.add_argument('dir', type=str, help="Will put you in username's home directory")
#         parser.add_argument('..', type=str, help="Will move you up one directory")
#         parser.add_argument('-', type=str, help="Will switch you to the previous directory", nargs='*')
#     elif sys.argv[1] == 'pwd':
#         parser.add_argument('-L', '--logical', type=str, help='use PWD from environment, even if it contains symlinks')
#         parser.add_argument('-P', '--physical', type=str, help="avoid all symlinks")
#     elif sys.argv[1] == 'printenv':
#         parser.add_argument('-0', '--null', type=str, help="End each output line with 0 byte rather than newline")
#     elif sys.argv[1] == 'export':
#         parser.add_argument('-p', help="List of all names that are exported in the current shell")
#         parser.add_argument('-n', help="Remove names from export list")
#         parser.add_argument('-f', help="Names are exported as functions")
#     elif sys.argv[1] == 'unset':
#         parser.add_argument('-p', help="List of all names that are exported in the current shell")
#         parser.add_argument('-n', help="Remove names from export list")
#         parser.add_argument('-f', help="Names are exported as functions")
#     elif sys.argv[1] == 'exit':
#         print('Put the exit_functions here')
#     args = parser.parse_args()
#     return args
