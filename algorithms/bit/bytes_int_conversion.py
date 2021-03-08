from collections import deque


def int_to_bytes_big_endian(num):
    bytestr = deque()
    while num > 0:
        # list.insert(0, ...) is inefficient
        bytestr.appendleft(num & 0xff)
        num >>= 8
    return bytes(bytestr)


def int_to_bytes_little_endian(num):
    bytestr = []
    while num > 0:
        bytestr.append(num & 0xff)
        num >>= 8
    return bytes(bytestr)


def bytes_big_endian_to_int(bytestr):
    num = 0
    for _b in bytestr:
        num <<= 8
        num += _b
    return num


def bytes_little_endian_to_int(bytestr):
    num = 0
    _e = 0
    for _b in bytestr:
        num += _b << _e
        _e += 8
    return num
