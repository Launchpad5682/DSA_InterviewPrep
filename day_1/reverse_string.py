# Reversing a string recursively

def reverseStringRecursive(str):

    if len(str) <= 1:
        return str

    return reverseStringRecursive(str[1:]) + str[0]

str = input("Enter a string: ")
print(reverseStringRecursive(str))