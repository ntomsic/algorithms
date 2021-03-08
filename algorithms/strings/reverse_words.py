def reverse(array, i, j):
    while i < j:
        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1


def reverse_words(string):
    arr = string.strip().split()  # arr is list of words
    _n = len(arr)
    reverse(arr, 0, _n - 1)

    return " ".join(arr)


if __name__ == "__main__":
    TEST = "I am keon kim and I like pizza"
    print(TEST)
    print(reverse_words(TEST))
