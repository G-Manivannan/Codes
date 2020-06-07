pos = -1

def search(list, n):
    l = 0                    # this is lower bound
    u = len(list)-1          # upper bound

    while l <= u:
        mid = (l+u) // 2         # finding mid index

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid+1
            else:
                u = mid-1

    return False


list = [4,7,8,12,45,99,1002,1025,1365]
n = 1365

if search(list, n):
    print("Found at", pos)
else:
    print("Not Found")