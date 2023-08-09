"""module countsort
   AKA, alternative sorting algorithm
"""


def countingSort(arr):
    """returns an array of elements i"""
    freq = [0] * (max(arr) + 1)
    for i in range(max(arr) + 1):
        freq[i] = arr.count(i)
    return freq


print(countingSort([5, 4, 3, 1, 1]))
