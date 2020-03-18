import pprint


INDENT = " "


SIGNS = {
    "unchanged": " ",
    "nested": " ",
    "removed": "-",
    "added": "+",
}


def stringify(value, depth):
    if type(value) is bool:
        return 'true' if value else 'false'

    if type(value) is not dict:
        return value

    def fn(item):
        key, value = item
        node = {
            'type': 'unchanged',
            'key': key,
            'old_value': value,
        }
        return node_to_string[node['type']](node, depth + 1)

    mapped = map(fn, value.items())
    body = '\n'.join(mapped)
    ind = get_indents(get_curly_brace_indents_count(depth + 1))
    result = "{{\n{body}\n{ind}}}".format(body=body, ind=ind)
    return result


def get_indents(count):
    return INDENT * count


def get_curly_brace_indents_count(depth):
    return 4 * depth


def get_block_indents_count(depth):
    return (4 * depth) + 2


def get_node_string(depth, node_type, key, value):
    block_indent = get_indents(get_block_indents_count(depth))
    sign = SIGNS[node_type]
    return "{indent}{sign} {key}: {value}".format(
        indent=block_indent, sign=sign, key=key, value=stringify(value, depth),
    )


node_to_string = {
    'removed': (lambda node, depth, _inner=None:
        get_node_string(depth, node["type"], node["key"], node["old_value"])),
    'added': (lambda node, depth, _inner=None:
        get_node_string(depth, node["type"], node["key"], node["new_value"])),
    'nested': (lambda node, depth, inner:
        get_node_string(
            depth, node["type"], node["key"],
            inner(node["children"], depth + 1),
        )),
    'unchanged': (lambda node, depth, _inner=None:
        get_node_string(depth, node["type"], node["key"], node["old_value"])),
    'changed': (lambda node, depth, _inner=None:
        "{old}\n{new}".format(
            old=get_node_string(depth, 'removed', node["key"], node["old_value"]),
            new=get_node_string(depth, 'added', node["key"], node["new_value"]),
        ))
}


def formatter(structure):
    def inner(substructure, depth):
        output = map(
            lambda node: node_to_string[node['type']](node, depth, inner),
            substructure,
        )

        flattened_lines = []

        def remove_nestings(l):
            for i in l:
                if type(i) is list:
                    remove_nestings(i)
                else:
                    flattened_lines.append(i)

        remove_nestings(list(output))

        body = '\n'.join(flattened_lines)
        ind = get_indents(get_curly_brace_indents_count(depth))
        result = "{{\n{body}\n{ind}}}".format(body=body, ind=ind)
        return result

    return inner(structure, 0)
