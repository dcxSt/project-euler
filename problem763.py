import numpy as np

def split_blob(blob):
    x = np.array([1,0,0])
    y = np.array([0,1,0])
    z = np.array([0,0,1])
    return np.array([ blob + x , blob + y , blob + z ])



state1 = np.array([[0,0,1],[0,1,0],[1,0,0]])
states = [state1]
n = 1

while True:
    # print(n)
    print("\n")
    for i in states:print(i.shape)
    # print(states)
    input("[Enter to continue]")

    new_states = []
    for state in states:
        # for each possible state of ameobas, branch
        for idx,blob in enumerate(state):
            # split each ameoba / blob into three
            new_blobs = split_blob(blob)
            acceptable = True
            for a in new_blobs:
                for b in state:
                    # verify to see if this split is allowed
                    if (a==b).all():
                        acceptable = False
                        break
                if acceptable==False:
                    break
                # since it can split, verify to see if this state has already beendone 
                new_state = np.concatenate([ new_blobs , state[:idx] , state[idx+1:] ])
                new_state = new_state[np.argsort(new_state[:,2])]
                new_state = new_state[np.argsort(new_state[:,1])]
                new_state = new_state[np.argsort(new_state[:,0])]
                for nstate in new_states:
                    if (new_state == nstate).all():
                        acceptable = False
                    break
            if acceptable:
                new_states.append( new_state )

    states = new_states
    n += 1
    print(n,len(states))
                    


