import json
import yaml

PARSERS = {
    '.json': json.load,
    '.yaml': yaml.load,
    '.yml': yaml.load,
}


def get_parser(ext):
    return PARSERS[ext]
