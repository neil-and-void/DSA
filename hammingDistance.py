'''
idea: use n & (n-1) to count all 0's
follow up: if we are to call this function many time, we can have a hash table
           and split the number into 4 partitions of the input and record each
           count result into the table

def hammingWeight(n: int) -> int:
    get mask of each 8 bit partition
    total
    for each of the partitions
        check if cached in hamming weights
        else, compute it
        add total
    return total
'''
from typing import *
def hammingWeight(n: int) -> int:
    mask = 0x000000ff
    totalHam = 0
    hammingWeights ={}

    for i in range(4):
        partition = n & mask
        if partition in hammingWeights:
            totalHam += hammingWeights[partition]
        else:
            hamWeight = countOnes(partition)
            hammingWeights[partition] = hamWeight
            totalHam += hamWeight
        mask <<= 8

    return totalHam

def countOnes(n):
    count = 0
    while n > 0:
        n = n & (n - 1)
        count += 1
    return count

n = 0b11111111111111111111111111111101
ans = hammingWeight(n)
print(ans)
