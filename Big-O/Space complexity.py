# Space complexity O(1)
def scary(n):
    for i in range(n):
        print("Boo!")


scary(6)

# Space complexity O(n)
def printHi(x):
    array = []
    for i in range(x):
        array.append("hi")
    print(array)


printHi(6)
