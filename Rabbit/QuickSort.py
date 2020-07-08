
# Stability: stable sorting algorithms maintain the relative order of records with equal keys (i.e., values).
# https://www.geeksforgeeks.org/python-program-for-quicksort/
# https://www.youtube.com/watch?v=PgBzjlCcFvc (搭配這個看就懂了)


"""
Complexity:
- Best: nlog(n)
- Avg: nlog(n)
    - 前面的n應該是指for loop NO!, 應該是指log(n)要執行n次
- Worst: n^2
"""


"""
思路：
- 這邊是要移smaller ones, 移到左區
- i 是"smaller zone的界線"

"""
# partition = partition the smaller & the larger
def partition(nums, low, high):

    pivot = nums[high]
    i = low - 1

    for j in range(low, high):
        if nums[j] <= pivot:
            i += 1
            nums[j], nums[i] = nums[i], nums[j]
    
    nums[high], nums[i + 1] = nums[i + 1], nums[high]
    
    return i + 1


def quickSort(arr,low,high): 
    if low < high: 
  
        pi = partition(arr,low,high) 

        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 