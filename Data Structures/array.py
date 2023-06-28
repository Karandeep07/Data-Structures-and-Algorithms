# Arrays are one of the most commonly-used data structures
# The elements of an array are stored in contiguous memory locations
# Arrays are of two types : Static and Dynamic
# Static arrays have fixed, pre-defined amount of memory that they can use, whereas in dynamic arrays this is flexible
# In Python we only have dynamic arrays

# BASIC OPERATIONS

arr = ['a', 'b', 'c', 'd']
print(arr[2])

first_element = arr[0]  # Indexing O(1)

# Push
arr.append('e')  # O(1)
print(arr)

# In some special cases, the append(push) operation may take greater time. This is because as mentioned earlier, Python has dynamic arrays
# So when an element is to appended and the array is filled, the entire array has to be copied to a new location
# With more space allocated(generally double the space) this time so that more items can be appended.
# Therefore, some individual operations may require O(n) time or greater, but when averaged over a large number of operations,
# The complexity can be safely considered to be O(1)

# Pop
arr.pop()  # O(1)
print(arr)  # Removes last element

# Insert: insert anywhere in array
# Syntax : insert(index, value)
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


# Array native python methods :

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy() 	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()     Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
