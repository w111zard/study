def is_key_exists(boxes):
    if boxes == "key":
        return True

    if boxes == None:
        return False

    for box in boxes:
        if is_key_exists(box):
            return True

    return False


boxes_without_key = [[[None, None], None, [[None], None]], [None], [[None], None], None, [[None]]]

boxes_with_key = [[[None, None], None, [[None], "key"]], [None], [[None], None], None, [[None]]]

print(is_key_exists(boxes_without_key))
print(is_key_exists(boxes_with_key))
