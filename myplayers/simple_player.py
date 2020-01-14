import random

is_last = False

while not is_last:

    '''
    read status
    '''

    # this is for catching EOFError when remaining gold is zero
    try:
        agent_id = int(input())
    except EOFError:
        break
    
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
    gold_detect = []
    gold_detect_amount = []
    for i in range(tmp[0]):
        gold_detect.append((tmp[i*3+1], tmp[i*3+2]))
        gold_detect_amount.append(tmp[i*3+3])
        
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
    if step+1 == max_num_step or gold_remain == 0:
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
    simple policy

    - samurai
      * move to the closest gold
      * if there's no gold, stay close to closer dog 

    - dog
      * run after his samurai + some randomness
      * when found a gold, don't move until his samurai is closer
    '''
    
    action = None
    while action == None:

        # for dogs 
        if agent_id >= 2:
            agent_x, agent_y = agents[agent_id]
            
            # find out relative x and y diff from his samurai
            dx = agents[agent_id-2][0] - agent_x
            dy = agents[agent_id-2][1] - agent_y

            action = None

            if len(gold_known) > 0:
                for i in range(len(gold_known)):
                    d = abs(gold_known[i][0] - agent_x) +\
                        abs(gold_known[i][1] - agent_y)
                    if d == 0:
                        dxo = agents[(agent_id-1)%2][0] - agent_x
                        dyo = agents[(agent_id-1)%2][1] - agent_y
                        if abs(dx)+abs(dy)+1 > abs(dxo)+abs(dyo):
                            action = -1

            if action == None:
                if len(gold_detect) > 0:
                    dx = gold_detect[0][0] - agent_x
                    dy = gold_detect[0][1] - agent_y
                    if dx > 0:
                        if dy > 0:
                            action = check(7)
                        elif dy < 0:
                            action = check(5)
                        else:
                            action = check(6)
                    elif dx < 0:
                        if dy > 0:
                            action = check(1)
                        elif dy < 0:
                            action = check(3)
                        else:
                            action = check(2)
                    else:
                        if dy > 0:
                            action = check(0)
                        elif dy < 0:
                            action = check(4)
                        

            '''
            if random.random() < .2 and abs(dx)+abs(dy) > 4:
            
                if dx > 0:
                    if dy > 0:
                        action = check(7)
                    elif dy < 0:
                        action = check(5)
                    if action == None:
                        action = check(6)
                elif dx < 0:
                    if dy > 0:
                        action = check(1)
                    elif dy < 0:
                        action = check(3)
                    if action == None:
                        action = check(2)
                if action == None:
                    if dy > 0:
                        action = check(0)
                    elif dy < 0:
                        action = check(4)
            '''

            if action == None:
                action = check(actions[agent_id])
            
            if action == None:
                action = check(random.randint(0, 8))

        # for samurais
        if agent_id <= 1:

            agent_x, agent_y = agents[agent_id]
            
            if len(gold_known) > 0:
                # find closest gold
                min = field_size * 2
                min_id = -1
                for i in range(len(gold_known)):
                    d = abs(gold_known[i][0] - agent_x) +\
                        abs(gold_known[i][1] - agent_y)
                    if d < min:
                        min = d
                        min_id = i

                # set action
                dx = gold_known[min_id][0] - agent_x
                dy = gold_known[min_id][1] - agent_y

                action = None
                if dx > 0:
                    action = check(6)
                if action == None and dx < 0:
                    action = check(2)
                if action == None and dy > 0:
                    action = check(0)
                if action == None and dy < 0:
                    action = check(4)
                if action == None:
                    action = -1
                
            else:
                # find closest dog
                if abs(agents[2][0] - agent_x) +\
                   abs(agents[2][1] - agent_y) <\
                   abs(agents[3][0] - agent_x) +\
                   abs(agents[3][1] - agent_y):
                    closer_dog_id = 2
                else:
                    closer_dog_id = 3
                    
                # set action
                dx = agents[closer_dog_id][0] - agent_x
                dy = agents[closer_dog_id][1] - agent_y

                action = None
                if dx > 0:
                    action = check(6)
                if action == None and dx < 0:
                    action = check(2)
                if action == None and dy > 0:
                    action = check(0)
                if action == None and dy < 0:
                    action = check(4)
                if action == None:
                    action = -1
                    
    print(action, flush=True)
