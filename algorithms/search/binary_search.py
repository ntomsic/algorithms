#
# Binary search works for a sorted array.
# Note: The code logic is written for an array sorted in
#  increasing order.
# For Binary Search, T(N) = T(N/2) + O(1) // the recurrence relation
# Apply Masters Theorem for computing Run time complexity of recurrence relations : T(N) = aT(N/b) + f(N)
# Here, a = 1, b = 2 => log (a base b) = 1
# also, here f(N) = n^c log^k(n) //k = 0 & c = log (a base b) So, T(N) = O(N^c log^(k+1)N) = O(log(N))


def binary_search(array, query):
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (high + low) // 2
        val = array[mid]
        if val == query:
            return mid
        if val < query:
            low = mid + 1
        else:
            high = mid - 1
    return None


def binary_search_recur(array, low, high, val):
    if low > high:  # error case
        return -1
    mid = (low + high) // 2
    if val < array[mid]:
        return binary_search_recur(array, low, mid - 1, val)
    if val > array[mid]:
        return binary_search_recur(array, mid + 1, high, val)
    return mid
