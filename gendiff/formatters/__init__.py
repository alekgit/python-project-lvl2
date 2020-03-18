from .json import formatter as json_formatter
from .plain import formatter as plain_formatter


FORMATTERS = {
    'json': json_formatter,
    'plain': plain_formatter,
}


def get_formatter(format='json'):
    return FORMATTERS[format]
