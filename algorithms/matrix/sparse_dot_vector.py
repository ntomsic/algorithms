#! /usr/bin/env python3
import random
import time

"""
Suppose we have very large sparse vectors, which contains a lot of zeros and double .

find a data structure to store them
get the dot product of them
"""


def vector_to_index_value_list(vector):
    return [(i, v) for i, v in enumerate(vector) if v != 0.0]


def dot_product(iv_list1, iv_list2):
    product = 0
    p_1 = len(iv_list1) - 1
    p_2 = len(iv_list2) - 1

    while p_1 >= 0 and p_2 >= 0:
        i_1, v_1 = iv_list1[p_1]
        i_2, v_2 = iv_list2[p_2]

        if i_1 < i_2:
            p_1 -= 1
        elif i_2 < i_1:
            p_2 -= 1
        else:
            product += v_1 * v_2
            p_1 -= 1
            p_2 -= 1

    return product


def __test_simple():
    print(dot_product(vector_to_index_value_list([1., 2., 3.]),
                      vector_to_index_value_list([0., 2., 2.])))
    # 10


def __test_time():
    vector_length = 1024
    vector_count = 1024
    nozero_counut = 10

    def random_vector():
        vector = [0 for _ in range(vector_length)]
        for i in random.sample(range(vector_length), nozero_counut):
            vector[i] = random.random()
        return vector

    vectors = [random_vector() for _ in range(vector_count)]
    iv_lists = [vector_to_index_value_list(vector) for vector in vectors]

    time_start = time.time()
    for i in range(vector_count):
        for j in range(i):
            dot_product(iv_lists[i], iv_lists[j])
    time_end = time.time()

    print(time_end - time_start, 'seconds')


if __name__ == '__main__':
    __test_simple()
    __test_time()
