def txt_to_lines():
    with open('day7/input.txt') as f:
        lines = f.read().splitlines()
    return lines


def process_file_system(lines):
    fs = {}
    for line in lines:
        if line[0] == '$':
            # we're at command, time to exit this function
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
    f = file_sys
    for idx, ppp in enumerate(current_path):
        if idx == len(current_path) - 1:
            # pass by reference, this actually updates file_sys
            f[ppp] = fs
        else:
            # This repoints the var to a new object
            f = f[ppp]


def parse(lines):
    file_sys = {}
    current_path = []
    for idx in range(len(lines)):
        # for idx, line in enumerate(lines):
        line = lines[idx]
        if line[0] == '$':
            # this is a command
            cmds = line.split(' ')
            if cmds[1] == 'ls':
                # breakpoint()
                # output is going to be a list of directories and files
                fs = process_file_system(lines[idx+1:])
                put_fs_at_curr_path(file_sys, current_path, fs)
            elif cmds[1] == 'cd':
                # Looks like there is no hopping directories, thankfully
                dir = cmds[2]
                if dir == '..':
                    current_path.pop()
                else:
                    current_path.append(dir)
    return file_sys


def directory_sum(dirr):
    summ = 0
    for k, v in dirr.items():
        if type(v) is int:
            summ += v
        else:
            summ += directory_sum(v)
    return summ


def sn(file_system, max_val=100_000):
    summ = 0
    for k, v in file_system.items():
        if type(v) is dict:
            ds = directory_sum(v)
            if ds <= max_val:
                summ += ds
            summ += sn(v)
    return summ


def dirs_above_need(file_system, need) -> list:
    above_need = []

    for k, v in file_system.items():
        if type(v) is dict:
            if directory_sum(v) >= need:
                above_need.append(directory_sum(v))
            above_need = above_need + dirs_above_need(v, need)
    return above_need


def sn2(file_system, total=70_000_000, need=30_000_000):
    used = directory_sum(file_system)
    left = total - used
    to_clean = need - left
    an = dirs_above_need(file_system, to_clean)
    return min(an)


lines = txt_to_lines()
print(sn(parse(lines)))
print(sn2(parse(lines)))
