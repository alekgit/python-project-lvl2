# -*- coding:utf-8 -*-

"""gendiff script."""
import argparse


def main():
    """Run this script."""
    parser = argparse.ArgumentParser(
        description="Generate diff"
    )

    parser.add_argument(
        "first_file",
        help="path to first config"
    )
    parser.add_argument(
        "second_file",
        help="path to second config"
    )

     parser.parse_args()


if __name__ == '__main__':
    main()
