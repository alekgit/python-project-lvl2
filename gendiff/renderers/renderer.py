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
