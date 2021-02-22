# This is the implementation of binary search recursively

def binarySearchRecursive(arr, low, high, find):

    mid = int(low + (high-low)/2)

    if find < arr[mid]:
        return binarySearchRecursive(arr, low, mid-1, find)

    elif find > arr[mid]:
        return binarySearchRecursive(arr, mid+1, high, find)

    return mid


size = int(input("Enter the size of an array: "))

print("Enter a sorted array: ")
arr = list()
for i in range(size):
    n = input()
    arr.append(int(n))

find = int(input("Enter the number to find: "))
print(binarySearchRecursive(arr, 0, size, find))
