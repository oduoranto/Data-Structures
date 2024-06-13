
def binarySearch(arr, target):
    left, right = 0, len(arr)-1

    while left <= right:
        mid = (left + (right - left)) // 2
        if(arr[mid] == target):
            return target
        elif(arr[mid]< target):
            left = mid + 1
        
        else :
            right = target - 1

    return -1

arr = [15, 25, 35, 40, 45, 50, 60, 80, 89, 89]
target = 50
index = binarySearch(arr, target)

if index != -1:
    print(f"Target {target} found at index {index}.")
else:
    print(f"Target {target} not found in the list.")
