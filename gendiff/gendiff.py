import os
from gendiff.parsers import get_parser
from gendiff.builder import build_diff
from gendiff.formatters import get_formatter


def generate_diff(path_to_first_file, path_to_second_file, format='json'):
    content1 = open(path_to_first_file)
    content2 = open(path_to_second_file)
    _, ext1 = os.path.splitext(path_to_first_file)
    _, ext2 = os.path.splitext(path_to_second_file)
    obj1 = get_parser(ext1)(content1)
    obj2 = get_parser(ext2)(content2)
    diff = build_diff(obj1, obj2)
    return get_formatter(format)(diff)
