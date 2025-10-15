

def ft_tqdm(lst: range) -> None:
    """
    reproduce the behavior of the official tqdm function that simulate a
    loading bar from numbers of a range given in parameter
    return None
    """
    for i, number in enumerate(lst):
        percentage = int(((i + 1) / lst.__len__()) * 100)
        loading = str(percentage) + '%|' + '█' * (percentage) + ' ' * \
            (100 - percentage) + '| ' + \
            str(i + 1) + '/' + str((lst.start - lst.stop).__abs__())
        print(f"{loading}", end='\r')
        yield number
