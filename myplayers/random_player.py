import random

is_last = False

while not is_last:

    '''
    read status
    '''

    agent_id = int(input())
    field_size = int(input())
    step  = int(input())
    max_num_step  = int(input())

    tmp = [int(x) for x in input().split()]
    holes = []
    for i in range(tmp[0]):
        holes.append((tmp[i*2+1], tmp[i*2+2]))

    tmp = [int(x) for x in input().split()]
    gold_known = []
    gold_known_amount = []
    for i in range(tmp[0]):
        gold_known.append((tmp[i*3+1], tmp[i*3+2]))
        gold_known_amount.append(tmp[i*3+3])
        
    tmp = [int(x) for x in input().split()]
    gold_found = []
    gold_found_amount = []
    for i in range(tmp[0]):
        gold_found.append((tmp[i*3+1], tmp[i*3+2]))
        gold_found_amount.append(tmp[i*3+3])
        
    tmp = [int(x) for x in input().split()]
    agents = []
    for i in range(4):
        agents.append((tmp[i*2], tmp[i*2+1]))
        
    plans = [int(x) for x in input().split()]

    actions = [int(x) for x in input().split()]

    scores = [int(x) for x in input().split()]

    gold_remain = int(input())
    
    time_remain = int(input())

    # last step?
    if step+1 == max_num_step:
        is_last = True

        
    '''
    YOU NEED TO CHANGE THE CODE BELOW
    '''

    # check if the chosen action is valid
    def check(action):

        x = agents[agent_id][0] 
        y = agents[agent_id][1]

        if action == 0:
            y += 1
        elif action == 1:
            y += 1
            x -= 1
        elif action == 2:
            x -= 1
        elif action == 3:
            y -= 1
            x -= 1
        elif action == 4:
            y -= 1
        elif action == 5:
            y -= 1
            x += 1
        elif action == 6:
            x += 1
        elif action == 7:
            y += 1
            x += 1

        if x >= field_size or x < 0 or \
           y >= field_size or y < 0:
            # out of field
            return None

        elif (x, y) in agents:
            # collision
            return None
        
        elif (x, y) in gold_known:
            if agent_id <= 1:
                # dig if agent is samurai
                return(action+8)
            else:
                # invalid if agent is dog
                return None

        elif (x, y) in holes:
            if agent_id <= 1:
                # fill if agent is samurai
                return(action+16)
            else:
                # invalid if agent is dog
                return(None)

        # just move
        return(action)


    '''        
    random policy
    '''
    
    action = None
    while action == None:

        # for dogs 
        if agent_id >= 2:
            action = check(random.randint(0, 8))

        # for samurais
        if agent_id <= 1:
            action = check(random.randint(0, 4) * 2)
        
    print(action, flush=True)
