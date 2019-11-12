import os, random

cnt = 0
is_last = False

while not is_last:

    a = [input().split() for x in range(13)]

    # last step
    if int(a[2][0])+1 == int(a[3][0]):
        is_last = True

    # choose random number from 0, 2, 4, 6
    print(random.randint(0, 3)*2, flush=True)


