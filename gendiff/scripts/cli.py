# -*- coding:utf-8 -*-

"""gendiff script."""
import argparse
from gendiff.gendiff import generate_diff


def main():
    """Run this script."""
    parser = argparse.ArgumentParser(
        description='Generate diff',
    )

    parser.add_argument(
        'path_to_first_file',
        help='path to first config',
    )
    parser.add_argument(
        'path_to_second_file',
        help='path to second config',
    )

    parser.add_argument(
        '-f', '--format',
        help='set format of output',
        choices=['plain', 'json'],
        default='json',
    )

    args = vars(parser.parse_args())
    print(generate_diff(**args))


if __name__ == '__main__':
    main()
