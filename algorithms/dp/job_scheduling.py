# Python program for weighted job scheduling using Dynamic
# Programming and Binary Search

# Class to represent a job
class Job:
    def __init__(self, start, finish, profit):
        self.start = start
        self.finish = finish
        self.profit = profit


# A Binary Search based function to find the latest job
# (before current job) that doesn't conflict with current
# job.  "index" is index of the current job.  This function
# returns -1 if all jobs before index conflict with it.
# The array jobs[] is sorted in increasing order of finish
# time.
def binary_search(job, start_index):
    # Initialize 'lo' and 'hi' for Binary Search
    low = 0
    high = start_index - 1

    # Perform binary Search iteratively
    while low <= high:
        mid = (low + high) // 2
        if job[mid].finish <= job[start_index].start:
            if job[mid + 1].finish <= job[start_index].start:
                low = mid + 1
            else:
                return mid
        else:
            high = mid - 1
    return -1


# The main function that returns the maximum possible
# profit from given array of jobs
def schedule(job):
    # Sort jobs according to finish time
    job = sorted(job, key=lambda j: j.finish)

    # Create an array to store solutions of subproblems.  table[i]
    # stores the profit for jobs till arr[i] (including arr[i])
    _n = len(job)
    table = [0 for _ in range(_n)]

    table[0] = job[0].profit

    # Fill entries in table[] using recursive property
    for i in range(1, _n):

        # Find profit including the current job
        incl_prof = job[i].profit
        _l = binary_search(job, i)
        if _l != -1:
            incl_prof += table[_l]

        # Store maximum of including and excluding
        table[i] = max(incl_prof, table[i - 1])

    return table[_n - 1]
