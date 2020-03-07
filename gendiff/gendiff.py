from gendiff.parsers.parser import parse
from gendiff.renderers.renderer import render
from gendiff.builder import buildInnerStructure


def generate_diff(first_file, second_file, format):
    content1 = open(first_file)
    content2 = open(second_file)
    obj1 = parse(content1)
    obj2 = parse(content2)
    inner_structure = buildInnerStructure(obj1, obj2)
    rendered = render(inner_structure)
    return rendered
