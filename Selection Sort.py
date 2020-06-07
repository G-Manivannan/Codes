

def sort(nums):

    for i in range(6):
        minpos = i
        for j in range(i,7):
            if nums[j] < nums[minpos]:
                minpos = j
        #swap

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

        print(nums)


nums = [5,3,8,6,9,15,2]
sort(nums)
print(nums)