import day6 as sut


def test_sn():
    assert sut.sn('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 7
    assert sut.sn('bvwbjplbgvbhsrlpgdmjqwftvncz') == 5
    assert sut.sn('nppdvjthqldpwncqszvftbrmjlhg') == 6
    assert sut.sn('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 10
    assert sut.sn('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 11
