def bitonic_sort(arr, reverse=False):
    """
    bitonic sort is sorting algorithm to use multiple process, but this code not containing parallel process
    It can sort only array that sizes power of 2
    It can sort array in both increasing order and decreasing order by giving argument true(increasing) and false(decreasing)

    Worst-case in parallel: O(log(_n)^2)
    Worst-case in non-parallel: O(nlog(_n)^2)

    reference: https://en.wikipedia.org/wiki/Bitonic_sorter
    """

    def compare(arr, reverse):
        _n = len(arr) // 2
        for i in range(_n):
            if reverse != (arr[i] > arr[i + _n]):
                arr[i], arr[i + _n] = arr[i + _n], arr[i]
        return arr

    def bitonic_merge(arr, reverse):
        _n = len(arr)

        if _n <= 1:
            return arr

        arr = compare(arr, reverse)
        left = bitonic_merge(arr[:_n // 2], reverse)
        right = bitonic_merge(arr[_n // 2:], reverse)
        return left + right

    # end of function(compare and bitionic_merge) definition
    _n = len(arr)
    if _n <= 1:
        return arr
    # checks if _n is power of two
    if not (_n and (not (_n & (_n - 1)))):
        raise ValueError("the size of input should be power of two")

    left = bitonic_sort(arr[:_n // 2], True)
    right = bitonic_sort(arr[_n // 2:], False)

    arr = bitonic_merge(left + right, reverse)

    return arr
