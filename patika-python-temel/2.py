def reverse_lists(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.append(reverse_lists(item))
        else:
            result.append(item)
    return result[::-1]

input_list = [[1, 2], [3, 4], [5, 6, 7]]
print(reverse_lists(input_list))