def BinarySearch(search_list, start_size, end_size, key):
    if end_size >= start_size:
        mid = (start_size + end_size)//2
        if search_list[mid][1] == key:
            return search_list[mid][0]
        elif search_list[mid][1] > key:
            return BinarySearch(search_list, start_size, mid - 1, key)
        else:
            return BinarySearch(search_list, mid + 1, end_size, key)
    else:
        return -1

new_list = [1, 2, 3]
new_list = list(enumerate(new_list))
end = len(new_list) - 1
print(BinarySearch(new_list, 0, end, 3))