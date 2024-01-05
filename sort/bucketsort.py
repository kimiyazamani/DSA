def bucket_sort(arr):
    
    max_val = max(arr)
    min_val = min(arr)

    bucket_range = (max_val - min_val) / len(arr)

    buckets = [[] for _ in range(len(arr))]

    for num in arr:
        index = int((num - min_val) / bucket_range)
        buckets[index].append(num)

    sorted_list = []
    for bucket in buckets:
        sorted_list.extend(sorted(bucket))

    return sorted_list