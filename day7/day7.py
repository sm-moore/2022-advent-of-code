def txt_to_lines():
    with open('day7/input.txt') as f:
        lines = f.read().splitlines()
    return lines


def process_fs(lines):
    fs = {}
    for line in lines:
        if line[0] == '$':
            # we're at command, time to exit this inner loop
            breakpoint()
            return fs
        else:
            components = line.split(' ')
            if components[0] == 'dir':
                fs[components[1]] = {}
            else:
                # file
                fs[components[1]] = int(components[0])
    return fs


def put_fs_at_curr_path(file_sys, current_path, fs):
    # file_sys[current_path[0]][current_path[1]] = fs
    # breakpoint(0)
    f = file_sys
    for idx, ppp in enumerate(current_path):
        if idx == len(current_path) - 1:
            # because python is pass by reference, this actually updates file_sys 
            f[ppp] = fs
        else:
            f = f[ppp]


def parse(lines):
    file_sys = {}
    current_path = []
    for idx in range(len(lines)):
    # for idx, line in enumerate(lines):
        line = lines[idx]
        if line[0] == '$':
            # this is a command
            command = line.split(' ')[1]
            if command == 'ls':
                # output is going to be a list of directories and files
                next_cmd_idx = lines[idx+1:].index('$') + idx + 1
                fs = process_fs(lines[idx+1:next_cmd_idx])

            

