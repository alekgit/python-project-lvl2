import json
from gendiff import __version__
from gendiff.gendiff import generate_diff


def test_version():
    assert __version__ == '0.1.0'

PATH_TO_BEFORE_FILE = 'tests/fixtures/before.json'
PATH_TO_AFTER_FILE = 'tests/fixtures/after.json'
PATH_TO_EXPECTED_FILE = 'tests/fixtures/expected'

def test_gendiff():
    expected = open(PATH_TO_EXPECTED_FILE).read()
    # obj1 = json.load(open(PATH_TO_BEFORE_FILE))
    # obj2 = json.load(open(PATH_TO_AFTER_FILE))
    actual = generate_diff(PATH_TO_BEFORE_FILE, PATH_TO_AFTER_FILE, 'plain')
    assert actual == expected
