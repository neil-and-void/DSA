def isEscapePossible(blocked, source, target):
    invalid = set()

    for pair in block:
        invalid.add(tuple(pair))

    current = source
    return isEscapePossibleRec(current, target, invalid)

def isEscapePossibleRec(current, target, invalid):

    ### base
    if current == target:
        return True

    # top
    if current[1] > 999999 or current[1] < 0 or current[0] > 999999 or current[0] < 0:
        return False

    # visited TODO
    if tuple(current) in invalid:
        return False

    ### recursive
    else:
        invalid.add(tuple(current))

        upCoords = [current[0], current[1] + 1]
        up = isEscapePossibleRec(upCoords, target, invalid)
        downCoords = [current[0], current[1] - 1]
        down = isEscapePossibleRec(downCoords, target, invalid)
        rightCoords = [current[0] + 1, current[1]]
        right = isEscapePossibleRec(rightCoords, target, invalid)
        leftCoords = [current[0] - 1, current[1]]
        left = isEscapePossibleRec(leftcoords, target, invalid)

        return up or down or right or left

