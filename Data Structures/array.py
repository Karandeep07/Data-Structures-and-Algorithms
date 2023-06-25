# Arrays are one of the most commonly-used data structures
# The elements of an array are stored in contiguous memory locations
# Arrays are of two types : Static and Dynamic
# Static arrays have fixed, pre-defined amount of memory that they can use, whereas in dynamic arrays this is flexible
# In Python we only have dynamic arrays

# BASIC OPERATIONS

arr = ['a', 'b', 'c', 'd']
print(arr[2]) 

first_element = arr[0]  # Indexing O(1)

# push
arr.append('e')  # O(1)
print(arr)

# In some special cases, the append(push) operation may take greater time. This is because as mentioned earlier, Python has dynamic arrays
# So when an element is to appended and the array is filled, the entire array has to be copied to a new location
# With more space allocated(generally double the space) this time so that more items can be appended.
# Therefore, some individual operations may require O(n) time or greater, but when averaged over a large number of operations,
# The complexity can be safely considered to be O(1)

# pop
arr.pop()  # O(1)
print(arr)  # Removes last element

# insert
# insert anywhere in array
# Syntax
arr.insert(0, 'x')  # O(n)
print(arr)

# Delete
arr.pop(0)  # Pops the first element of the array. O(n)
print(arr)

# Removes the first occurrence of the element 'c' in the array. O(n)
arr.remove('c')
print(arr)

arr1 = ['a', 'b', 'c', 'd']
del arr1[1:3]  # Deletes elements from position 1 to position 2. O(n)
print(arr1)


# Implementation
    # Although arrays are pre-defined in Python in the form of lists, we can implement our own arrays.

# Here, we will implement our own array with some common methods such as access, push, pop, insert, delete

