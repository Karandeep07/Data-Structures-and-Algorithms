# O(1) - Constant Time

# Eg: 1
import time

array_small = ['nemo' for i in range(10)]
array_medium = ['nemo' for i in range(100)]
array_large = ['nemo' for i in range(100000)]


def finding_nemo(array):
    t0 = time.time()
    print(array[0])  # O(1) operation
    print(array[1])  # O(1) operation
    t1 = time.time()
    print(f'Time taken = {t1-t0}')


finding_nemo(array_small)
finding_nemo(array_medium)
finding_nemo(array_large)
