# Log all pairs of array
boxes = ['a', 'b', 'c', 'd', 'e']


def log_all_pairs_of_array(array):
    for i in range(len(array)):  # O(n)
        for j in range(len(array)):  # O(n)
            print(array[i], array[j])


log_all_pairs_of_array(boxes)


# We ignore smaller degree terms and constants in Big-O notation to focus on the highest degree term.
# when 2 loops are nested, it becomes multiplication
# O(n * n) => O(n^2)
