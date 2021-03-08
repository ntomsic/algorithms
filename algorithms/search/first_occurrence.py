#
# Find first occurance of a number in a sorted array (increasing order)
# Approach- Binary Search
# T(n)- O(log n)
#
def first_occurrence(array, query):
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        # print("lo: ", lo, " hi: ", hi, " mid: ", mid)
        if low == high:
            break
        if array[mid] < query:
            low = mid + 1
        else:
            high = mid
    if array[low] == query:
        return low
