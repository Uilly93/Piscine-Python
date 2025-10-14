from time import sleep


array = range(333)


def ft_load(array: range):
    count = 0
    for number in array:
        count = int((number / (array.stop) * 100) + 1).__abs__()
        yield count


def ft_tqdm(lst: range) -> None:
    # counter = ft_load(array)
    loading: str = ''
    for i, number in enumerate(lst):
        percentage = int((number / lst.__len__()) * 100)
        space = ''
        if str(number).__len__() == 2:
            space = ' '
        elif str(number).__len__() == 1:
            space = '  '
        loading = space + str(percentage) + '|' + '█' * (number + 1) + ' ' * \
            (100 - number) + '| ' + \
            str((array.start) * number) + '/' + str(array.stop)
        print(f"{loading}", end='\r')
        yield number
        # print(f"{space}{number}%: {loading}", end='\r')
        # sleep(0.04)
    # print(f"{number}%: {loading}")
