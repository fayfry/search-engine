def sortitout(lists):

    #  lists is a list of sorted lists IT CANNOT HAVE EMPTY LISTS

    iterators = []  # iterators for each list in list_of_lists
    firsts = []  # list offirst elements of iterated lists

    for l in lists:
        iterators.append(iter(l))

    for iter_list in iterators:
        firsts.append(next(iter_list))

    while firsts:
        minim = min(firsts)  # new min could be added

        # to get the next element in a list that provided the latest min element
        extracted = firsts.index(minim)
        try:
            firsts[extracted] = next(iterators[extracted])
        except StopIteration:
            firsts.pop(extracted)
            iterators.pop(extracted)
        yield minim