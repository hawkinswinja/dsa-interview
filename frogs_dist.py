"""
There are n blocks, numbered from 0 to n-1, arranged in a row. 
A couple of frogs were sitting together on one block when they had a terrible quarrel. 
Now they want to jump away from one another so that the distance between them will be as large as possible.
The distance between blocks numbered j and k, where j ≤ k, is computed as k − j + 1. 
The frogs can only jump up, meaning that they can move from one block to another only if the two blocks are adjacent
and the second block is of the same or greater height as the first.
What is the longest distance that they can possibly create between each other, 
if they also chose to sit on the optimal starting block initially?
"""

def max_frog_distance(blocks):
    max_dist = 0
    for i in range(len(blocks)):
        max_dist = max(get_jumps(blocks, i), max_dist)
    return max_dist


def get_jumps(block, i):
    left = right = 0
    for j in range(i, len(block) - 1):
        if block[j + 1] < block[j]:
            break
        right += 1
    for j in range(i, -1, -1):
        if block[j - 1] < block[j] or j == 0:
            break
        left += 1
    return left + right + 1


blocks1 = [2, 6, 8, 5]
print(max_frog_distance(blocks1))  # Output: 3

blocks2 = [1, 5, 5, 2, 6]
print(max_frog_distance(blocks2))  # Output: 4

blocks3 = [1, 1]
print(max_frog_distance(blocks3))  # Output: 2
