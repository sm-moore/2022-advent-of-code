import day7 as sut


def test_directory_sum():
    expected = {
        '/': {
            'a': {
                'fi': 5
            }
        }}
    assert sut.directory_sum(expected) == 5

    expected2 = {
        '/': {
            'a': {
                'fi': 5,
                'b': {
                    'c': 10
                    }
            }
        }}
    assert sut.directory_sum(expected2) == 15

def test_sn_small():
    expected = {
        '/': {
            'a': {
                'fi': 5
            }
        }}
    assert sut.sn(expected) == 10

    expected2 = {
        '/': {
            'a': {
                'fi': 5,
                'b': {
                    'c': 10
                    }
            }
        }}
    assert sut.sn(expected2) == 40


def test_put_fs_at_curr_path():
    input = {'/': {
            'a': {
                'fi': 5,
                'b': {}
            }
        }}
    current_path = ['/', 'a', 'b']
    fs = {'c': 10}
    expected = {'/': {
            'a': {
                'fi': 5,
                'b': {'c': 10}
            }
        }}
    sut.put_fs_at_curr_path(input, current_path, fs)
    assert input == expected


def test_process_file_system():
    input = [
        '34044 cqldc.nmr',
        'dir drg',
        'dir gcfth',
        '266939 phcfhh'
    ]
    expected = {
        'cqldc.nmr': 34044,
        'drg': {},
        'gcfth': {},
        'phcfhh': 266939
    }
    assert sut.process_file_system(input) == expected


def test_parse_small():
    input = [
        '$ cd /',
        '$ ls',
        '5 a',
    ]
    expected = {
        '/': {
            'a': 5
        }}
    assert sut.parse(input) == expected

    input2 = [
        '$ cd /',
        '$ ls',
        'dir a',
        '$ cd a',
        '$ ls',
        '5 fi',
    ]
    expected2 = {
        '/': {
            'a': {
                'fi': 5
            }
        }}
    assert sut.parse(input2) == expected2


def test_parse():
    input = [
        '$ cd /',
        '$ ls',
        'dir a',
        '14848514 b.txt',
        '8504156 c.dat',
        'dir d',
        '$ cd a',
        '$ ls',
        'dir e',
        '29116 f',
        '2557 g',
        '62596 h.lst',
        '$ cd e',
        '$ ls',
        '584 i',
        '$ cd ..',
        '$ cd ..',
        '$ cd d',
        '$ ls',
        '4060174 j',
        '8033020 d.log',
        '5626152 d.ext',
        '7214296 k',
    ]
#  - / (dir)
#   - a (dir)
#     - e (dir)
#       - i (file, size=584)
#     - f (file, size=29116)
#     - g (file, size=2557)
#     - h.lst (file, size=62596)
#   - b.txt (file, size=14848514)
#   - c.dat (file, size=8504156)
#   - d (dir)
#     - j (file, size=4060174)
#     - d.log (file, size=8033020)
#     - d.ext (file, size=5626152)
#     - k (file, size=7214296)
    expected = {
        '/': {
            'a': {
                'e': {
                    'i': 584
                },
                'f': 29116,
                'g': 2557,
                'h.lst': 62596
            },
            'b.txt': 14848514,
            'c.dat': 8504156,
            'd': {
                'j': 4060174,
                'd.log': 8033020,
                'd.ext': 5626152,
                'k': 7214296
            }
        }
    }
    assert sut.parse(input) == expected


def test_sn():
    input = {
        '/': {
            'a': {
                'e': {
                    'i': 584
                },
                'f': 29116,
                'g': 2557,
                'h.lst': 62596
            },
            'b.txt': 14848514,
            'c.dat': 8504156,
            'd': {
                'j': 4060174,
                'd.log': 8033020,
                'd.ext': 5626152,
                'k': 7214296
            }
        }
    }
    assert sut.sn(input) == 95437


def test_sn2():
    input = {
        '/': {
            'a': {
                'e': {
                    'i': 584
                },
                'f': 29116,
                'g': 2557,
                'h.lst': 62596
            },
            'b.txt': 14848514,
            'c.dat': 8504156,
            'd': {
                'j': 4060174,
                'd.log': 8033020,
                'd.ext': 5626152,
                'k': 7214296
            }
        }
    }
    assert sut.sn2(input) == 24933642


def test_smallest_above_need():
    input = {
        '/': {
            'a': {
                'fi': 5,
                'b': {
                    'c': 10
                    }
            }
        }}
    assert sut.dirs_above_need(input, need=4) == [15, 15, 10]
