

def ft_tqdm(lst: range) -> None:
    array: list = lst
    loading: str = ''
    for i, number in enumerate(array):
        percentage = int(((i + 1) / lst.__len__()) * 100)
        loading = str(percentage) + '%|' + '█' * (percentage) + ' ' * \
            (100 - percentage) + '| ' + \
            str(i + 1) + '/' + str((lst.start - lst.stop).__abs__())
        print(f"{loading}", end='\r')
        yield number
