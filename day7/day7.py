def txt_to_lines():
    with open('day7/input.txt') as f:
        lines = f.read().splitlines()
    return lines


def process_ls(lines):
    """Given lines of input parse listed files/dirs until another command is
        reached.
        Returns a dictionary representing the file system as shown by ls.
        Directories will have a dict as the value, files will have an int.
    """
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
    """Given a file system dictionary and a list of strings representing the
    current path set fs at the current path in the file system.
    """
    f = file_sys
    for idx, ppp in enumerate(current_path):
        if idx == len(current_path) - 1:
            # pass by reference, this actually updates file_sys
            f[ppp] = fs
        else:
            # This repoints the var to a new object
            f = f[ppp]


def parse(lines):
    # Parse the input into a dictionary where dictionary values represent
    # dirs and int values represent files
    file_sys = {}
    current_path = []
    for idx, line in enumerate(lines):
        # process the commands
        if line[0] == '$':
            cmds = line.split(' ')
            if cmds[1] == 'ls':
                fs = process_ls(lines[idx+1:])
                # I'm sure this could be done recursively by traversing all
                # the way down the tree and building the file system on the
                # way up.
                put_fs_at_curr_path(file_sys, current_path, fs)
            elif cmds[1] == 'cd':
                # Looks like there is no skipping directories, thankfully
                # Part of why I didn't do the above recursively was because I
                # thought there would be skipping around ex. 'cd ../a'.
                change_to = cmds[2]
                if change_to == '..':
                    current_path.pop()
                else:
                    current_path.append(change_to)
    return file_sys


def directory_sum(dirr):
    # Sum of all nested files in the given directory
    summ = 0
    for k, v in dirr.items():
        if type(v) is int:
            summ += v
        else:
            summ += directory_sum(v)
    return summ


def sn(file_system, max_val=100_000):
    summ = 0
    for v in file_system.values():
        if type(v) is dict:
            ds = directory_sum(v)
            if ds <= max_val:
                summ += ds
            summ += sn(v)
    return summ


def dirs_above_need(file_system, need) -> list:
    above_need = []

    for v in file_system.values():
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
