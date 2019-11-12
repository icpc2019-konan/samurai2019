import random

is_last = False

while not is_last:

    # read status
    status = [input().split() for x in range(13)]

    # last step?
    if int(status[2][0])+1 == int(status[3][0]):
        is_last = True

    '''
    need to change below
    '''

    # choose random number from 0, 2, 4, 6
    print(random.randint(0, 3)*2, flush=True)
