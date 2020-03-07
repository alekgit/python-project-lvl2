def buildInnerStructure(obj1, obj2):
    keys = sorted((set().union(obj1.keys(), obj2.keys())))

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
