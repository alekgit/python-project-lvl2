from .json import formatter as json_formatter
from .plain import formatter as plain_formatter
import json


FORMATTERS = {
    'tree': json_formatter,
    'plain': plain_formatter,
    'json': json.dumps,
}


def get_formatter(format='json'):
    return FORMATTERS[format]
