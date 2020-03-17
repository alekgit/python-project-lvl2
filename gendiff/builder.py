import pprint


def build_node(node_type, key, old_value=None, new_value=None, children=None):
    return {
        'type': node_type,
        'key': key,
        'old_value': old_value,
        'new_value': new_value,
        'children': children,
    }


def build_diff(obj1, obj2):
    keys = sorted((set().union(obj1.keys(), obj2.keys())))

    def fn(key):
        if key not in obj1:
            return build_node('added', key, new_value = obj2[key])
        if key not in obj2:
            return build_node('removed', key, old_value = obj1[key])
        if type(obj2[key]) is dict and type(obj1[key]) is dict:
            old_value = obj1[key]
            new_value = obj2[key]
            children = build_diff(old_value, new_value)
            return build_node('nested', key, old_value, new_value, children)
        if obj1[key] == obj2[key]:
            return build_node('unchanged', key, obj1[key], obj2[key])
        return build_node('changed', key, obj1[key], obj2[key])

    nodes = map(fn, keys)
    return list(nodes)
