def in_array(array1, array2):
    r = []
    deduper = []
    result = []
    for i in array1:
        for k in array2:
            if i in k:
                r.append(i)

    for i in r:
        if i not in deduper:
            result.append(i)
        deduper.append(i)

    result.sort()

    return result
