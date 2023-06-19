# O(n) - Linear Time

# Eg: 1
import time

nemo = ['nemo']
everyone = ['dory', 'bruce', 'marlin', 'nemo',
            'gill', 'bloat', 'nigel', 'squirt', 'darla']
large = ['nemo' for i in range(100000)]


def find_nemo(array):
    t0 = time.time()
    for i in range(0, len(array)):
        if array[i] == 'nemo':
            print("Found Nemo!!")
    t1 = time.time()
    print(f'The search took {t1-t0} seconds.')


# find_nemo(nemo)
# find_nemo(everyone)
find_nemo(large)

# Eg: 2
def randomChallenge(input):
    temp = 10  # O(1)
    temp = 50 + 3  # O(1)

    for i in range(len(input)):
        stranger = True  # O(n)
        temp += 1  # O(n)

        return temp  # O(1)

# Big O (3+2n)
# Constants doesn't matter
# Big O(n)
