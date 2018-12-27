import subprocess  # Use run() to launch a program within a program
import resource  # Calculate memory allocation & run-time
import pstats  # Calculate the number of function calls, time per call
import argparse
import cProfile
# import importlib


def get_arg():  # Vu
    '''
    Get the arguments from the terminal.
    The function returns:
    + sub_program: the name of the evaluating program, type: str
    + memory_f: flag of -m mode, type: Boolean, default: False
    + time_f: flag of -t mode, type: Boolean, default: True
    + num_func_f: flag of -n mode, type: Boolean, deafult: False
    '''
    parser = argparse.ArgumentParser(description='Benchmark')
    parser.add_argument('-t', action='store_true',
                        help='outputs the execution time (run-time)\
                        of the target program', default=True)
    parser.add_argument('-m', action='store_true',
                        help='outputs the memory allocation\
                        of the target program', default=False)
    parser.add_argument('-n', action='store_true', help='outputs the number' +
                        'of function calls of the target program',
                        default=False)
    parser.add_argument('sub_program', action='store', type=str, nargs='+')
    ap = parser.parse_args()
    return ap.sub_program, ap.t, ap.m, ap.n


def get_run_time():  # Vu
    '''
    Get the run-time of evaluating program
    The function returns:
    + run_time: the run-time of evaluating program, type: Unknown, maybe int
    '''
    return resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime


def get_memory_use():  # Duc
    '''
    Get the memory usage of evaluating program
    The function returns:
    + mem_use: the memory usage of evaluating program, type: int
    '''
    return resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss


def get_num_funcs(sub_program):  # Duc
    '''
    Get the number of functions of evaluating program
    The function returns:
    + num_func: the number of functions of evaluating program, type: int
    '''
    # program_name = sub_program[0][2:-3]
    # filename = 'profile_stats.stats'
    # profile.run('importlib.import_module(\'{}\')'.format(program_name),\
    # filename)
    # stats = pstats.Stats(filename).strip_dirs().sort_stats('calls')
    # stats.print_stats(sub_program[0][2:])
    compile_target_file = compile(open(sub_program, "r").read(),
                                  sub_program, 'exec')
    pr = cProfile.Profile()
    pr.enable()
    pr.run(compile_target_file)
    pr.disable()
    ps = pstats.Stats(pr).strip_dirs().sort_stats('calls')
    ps.print_stats(sub_program.split('./')[1])
