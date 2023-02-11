def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):  # eğer döngüdeki item bir liste ise
            result.extend(flatten(item))  # recursive olarak döngüye sok
        else:
            result.append(item)  # değilse result listesine ekle
    return result


input_list = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
print(flatten(input_list))
