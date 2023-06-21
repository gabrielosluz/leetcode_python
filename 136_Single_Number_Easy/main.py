from typing import List
def singleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    a = 0
    for i in nums:
        a ^= i
    return a

singleNumber([2,2,1])

#outra solucao, mas que nao atende

def singleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    return 2 * sum(set(nums)) - sum(nums)

#mais uma solucao que nao atende
def singleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    no_duplicate_list = []
    for i in nums:
        if i not in no_duplicate_list:
            no_duplicate_list.append(i)
        else:
            no_duplicate_list.remove(i)
    return no_duplicate_list.pop()