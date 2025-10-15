def isNaN(num):
    return num != num


def NULL_not_found(object: any) -> int:
    x = type(None)
    objtype = type(object)
    if objtype is float and isNaN(object):
        print(f'Cheese: {object} {objtype}')
    elif objtype == x and object is None:
        print(f'Nothing: {object} {objtype}')
    elif objtype is str and object == '':
        print(f'Empty: {object} {objtype}')
    elif objtype is int and object == 0:
        print(f'Zero: {object} {objtype}')
    elif objtype is bool and object is False:
        print(f'Fake: {object} {objtype}')
    else:
        print("Type not found")
        return 1
    return 0
