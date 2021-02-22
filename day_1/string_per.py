# creating all the permutations of the given string

permutations = []

def stringPermutations(str, i, length):

    # add the complete permutation to the list
    if i == length:
        permutations.append(''.join(str))

    else:
        for j in range(i,length):
            # swap the elements
            str[i], str[j] = str[j],str[i]
            stringPermutations(str,i+1,length)
            # backtrack the swap
            str[i], str[j] = str[j], str[i]


str = input("Enter the string: ")
stringPermutations(list(str),0,len(str))
print(permutations)
print(len(permutations))