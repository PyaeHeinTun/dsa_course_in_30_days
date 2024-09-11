def rotate_list(arr:list,k):
    if k >= len(arr):
        return arr
    return arr[k:] + arr[:k]

def remove_duplicate(arr:list):
    prev_item = None
    unique_list = []
    arr.sort()

    for item in arr:
        if prev_item != item:
            unique_list.append(item)
        prev_item = item

    return unique_list

def merge_sorted_list(arr1:list,arr2:list):
    arr = arr1 + arr2
    arr = sorted(arr)
    return arr

def second_largest_number(arr:list):
    remove_dup_arr = list(set(arr))
    arr.sort()
    return arr[len(arr)-2] if len(remove_dup_arr) >= 2 else None

def find_pair_of_value_by_sum(arr:list,value:int):
    pair_list = []
    for i in range(0,len(arr)):
        for number in arr[i+1:]:
            if (arr[i]+number == value):
                pair_list.append((arr[i],number))
    return pair_list

def find_intersection_of_list(arr1:list,arr2:list):
    intersected_list = []
    for item1 in arr1:
        for item2 in arr2:
            if (item1 == item2):
                intersected_list.append(item1)
    return intersected_list

def find_longest_increasing_subsequence(arr:list):
    prev_largest_subsequence = 0
    longest_subsequence_list = []
    for item in arr:
        if (item > prev_largest_subsequence):
            longest_subsequence_list.append(item)
            prev_largest_subsequence = item

    return longest_subsequence_list