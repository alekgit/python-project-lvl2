def stringify(value):
    if type(value) is bool:
        return 'true' if value else 'false'
    if type(value) is dict:
        return 'complex value'
    return value


node_to_string = {
    'removed': (lambda node, path, _inner=None:
        "Property '{prop}' was removed".format(
            prop='.'.join([*path, node['key']]),
        )),
    'added': (lambda node, path, _inner=None:
        "Property '{prop}' was added with value: '{val}'".format(
            prop='.'.join([*path, node['key']]),
            val=stringify(node['new_value']),
        )),
    'nested': (lambda node, path, inner:
        inner([*path, node['key']], node['children'])),
    'unchanged': lambda node, path, _inner=None: [],  # для '' возвращает пустую строку
    'changed': (lambda node, path, _inner=None:
        "Property '{prop}' was changed from '{old_val}' to '{new_val}'".format(
            prop='.'.join([*path, node['key']]),
            old_val=stringify(node['old_value']),
            new_val=stringify(node['new_value']),
        ))
}


def formatter(structure):
    def inner(path, substructure):
        mapped = map(
            lambda node: node_to_string[node['type']](node, path, inner),
            substructure,
        )

        flattened_lines = []

        def remove_nestings(l):
            for i in l:
                if type(i) is list:
                    remove_nestings(i)
                else:
                    flattened_lines.append(i)

        remove_nestings(list(mapped))
        output = '\n'.join(flattened_lines)
        return output

    return inner([], structure)
