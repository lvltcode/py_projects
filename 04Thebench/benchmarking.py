#!/usr/bin/env python3
from benchmark_utils import *
import subprocess
sub_program, time_f, memory_f, num_func_f = get_arg()
if memory_f:
    subprocess.run(sub_program)
    mem_use = get_memory_use()
    print('Memory usage:', mem_use, 'kB')

elif num_func_f:
    get_num_funcs(sub_program[0])

elif time_f:
    subprocess.run(sub_program)
    run_time = get_run_time()
    print('Run-time:', run_time, 's')
