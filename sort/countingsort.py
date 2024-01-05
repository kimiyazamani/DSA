def counting_sort(arr):

    max_val = max(arr)

    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    sorted_list = []
    for i in range(len(count)):
        sorted_list.extend([i] * count[i])

    return sorted_list
