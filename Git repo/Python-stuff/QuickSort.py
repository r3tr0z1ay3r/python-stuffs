def quicksort1(arr):
    i = arr[0]
    j = arr[-1]
    mid = (len(arr)-1)//2
    if arr[j] < arr[i] and arr[i] < arr[mid]:
        pass
    for temp in range(i,mid-1):
        print(temp)
quicksort1([4,32,1,21,2,2])

def partition(l, r, nums):
    pivot, ptr = nums[r], l
    for i in range(l, r):
        if nums[i] <= pivot:
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
    nums[ptr], nums[r] = nums[r], nums[ptr]
    return ptr
def quicksort(l, r, nums):
    if len(nums) == 1:  
        return nums
    if l < r:
        pi = partition(l, r, nums)
        quicksort(l, pi-1, nums)  
        quicksort(pi+1, r, nums)  
    return nums
example = [4, 5, 1, 2, 3]
print(quicksort(0, len(example)-1, example))