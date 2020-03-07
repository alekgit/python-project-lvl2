import os
import json


def buildInnerStructure(obj1, obj2):
    keys = set().union(obj1.keys(), obj2.keys())

    nodes = []
    for key in keys:
        if key in obj1 and key in obj2:
            old_value = obj1[key]
            new_value = obj2[key]
            if old_value == new_value:
                node = {
                    "type": "unchanged",
                    "key": key,
                    "old_value": old_value,
                    "new_value": new_value,
                }
            else:
                node = {
                    "type": "changed",
                    "key": key,
                    "old_value": old_value,
                    "new_value": new_value,
                }
        else:
            if key in obj1:
                old_value = obj1[key]
                node = {
                    "type": "removed",
                    "key": key,
                    "old_value": old_value,
                    "new_value": None,
                }
            else:
                new_value = obj2[key]
                node = {
                    "type": "added",
                    "key": key,
                    "old_value": None,
                    "new_value": new_value,
                }
        nodes.append(node)

    return nodes


def render(inner_structure):
    tab = "  "
    signs = {
        "unchanged": " ",
        "changed":   "+",
        "removed":   "-",
        "added":     "+",
    }

    lines = []
    for node in inner_structure:
        node_type = node["type"]
        key = node["key"]
        old_value = node["old_value"]
        new_value = node["new_value"]
        if node_type == "unchanged":
            line = "{tab}{sign} {key}: {value}".format(
                tab=tab, sign=signs[node_type], key=key, value=old_value,
            )
        elif node_type == "changed":
            added_node_line = "{tab}{sign} {key}: {value}".format(
                tab=tab, sign=signs["added"], key=key, value=new_value,
            )
            removed_node_line = "{tab}{sign} {key}: {value}".format(
                tab=tab, sign=signs["removed"], key=key, value=old_value,
            )
            line = [added_node_line, removed_node_line]
        elif node_type == "removed":
            line = "{tab}{sign} {key}: {value}".format(
                tab=tab, sign=signs[node_type], key=key, value=old_value,
            )
        else:
            line = "{tab}{sign} {key}: {value}".format(
                tab=tab, sign=signs[node_type], key=key, value=new_value,
            )
        lines.append(line)

    flattened_lines = []

    def remove_nestings(l):
        for i in l:
            if type(i) == list:
                remove_nestings(i)
            else:
                flattened_lines.append(i)
    remove_nestings(lines)

    body = '\n'.join(flattened_lines)
    result = "{{\n{body}\n}}".format(body=body)

    return result


def generated_diff(first_file, second_file, format):
    obj1 = json.load(open(first_file))
    obj2 = json.load(open(second_file))

    inner_structure = buildInnerStructure(obj1, obj2)
    rendered = render(inner_structure)
    return rendered
