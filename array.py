s = [0] * 5

t = "hello" * 6

import sys
t = ["hello"]
s = "hello"
print(sys.getsizeof(s))
print(sys.getsizeof(t))


data = []
for k in range(2):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length: {0:3d}; Size in bytes:{1:4d}'.format(a,b))
    data.append(None)
