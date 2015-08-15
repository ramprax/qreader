from qreader.constants import MODE_SIZE_SMALL, MODE_SIZE_LARGE
from qreader.constants import MODE_SIZE_MEDIUM

__author__ = 'ewino'


def is_overlapping(rect1, rect2):
    hoverlaps = range_overlap(rect1[0], rect1[2], rect2[0], rect2[2])
    voverlaps = range_overlap(rect1[1], rect1[3], rect2[1], rect2[3])
    return hoverlaps and voverlaps


def range_overlap(a_min, a_max, b_min, b_max):
    """Neither range is completely greater than the other"""
    return (a_min <= b_max) and (b_min <= a_max)


# taken from qrcode package
def get_mask_func(mask_id):
    """
    Return the mask function for the given mask pattern.
    """
    id_to_mask = {
        0: lambda i, j: (i + j) % 2 == 0,  # 000
        1: lambda i, j: i % 2 == 0,  # 001
        2: lambda i, j: j % 3 == 0,  # 010
        3: lambda i, j: (i + j) % 3 == 0,  # 011
        4: lambda i, j: (i // 2 + j // 3) % 2 == 0,  # 100
        5: lambda i, j: (i * j) % 2 + (i * j) % 3 == 0,  # 101
        6: lambda i, j: ((i * j) % 2 + (i * j) % 3) % 2 == 0,  # 110
        7: lambda i, j: ((i * j) % 3 + (i + j) % 2) % 2 == 0,  # 111
    }
    if mask_id in id_to_mask:
        return id_to_mask[mask_id]
    raise TypeError("Bad mask pattern: " + mask_id)


def mode_sizes_for_version(version):
    if 0 < version < 10:
        return MODE_SIZE_SMALL
    elif version < 27:
        return MODE_SIZE_MEDIUM
    elif version <= 40:
        return MODE_SIZE_LARGE
    raise ValueError('Unknown QR version: %s' % (version,))


def bits_for_length(version, data_mode):
    size_mode = mode_sizes_for_version(version)

    if data_mode not in size_mode:
        raise TypeError("Unknown data type ID: %s" % (data_mode,))

    return size_mode[data_mode]
