import os
from gendiff.parsers import get_parser
from gendiff.builder import build_diff
from gendiff.renderers.renderer import render


def generate_diff(first_file, second_file, format='json'):
    content1 = open(first_file)
    content2 = open(second_file)
    _, ext1 = os.path.splitext(first_file)
    _, ext2 = os.path.splitext(second_file)
    obj1 = get_parser(ext1)(content1)
    obj2 = get_parser(ext2)(content2)

    diff = build_diff(obj1, obj2)
    # print(diff)
    return render(diff)
