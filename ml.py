
from copy import deepcopy
import time
from collections import Counter

# Initialize lists and variables
bl = []
al = []
his = []
action_limit = None




def ad(b):
    global bl, al
    bl.append(deepcopy(b))
    al.append(1)
def ml(b, m):
    global action_limit
    if not isinstance(m, bool):
        action_limit = m
    if b not in bl:
        ad(b)
    bidx = bl.index(b)
    if len(his) == 4:
        if m:
            al[his[-1]] += 1
        if al[bidx] > action_limit:
            al[bidx] = 1
            al[his[-1]] += 1
    his.append(bidx)
    if len(his) > 4:
        del his[0]
    return al[bidx]

CT=Counter()
first_tc,first_fc,last_fc,last_tc,f_rate,t_rate=0,0,0,0,0,0

def show_stats(m):
    global CT, last_fc, last_tc, f_rate, t_rate, first_tc, first_fc

    if 'frame' not in CT:
        CT['frame'] = 0
    if 'called' not in CT:
        CT['called'] = 0
    if 'true_count' not in CT:
        CT['true_count'] = 0
    if 'false_count' not in CT:
        CT['false_count'] = 0

    CT['called'] += 1
    if m:
        CT['true_count'] += 1
    else:
        CT['false_count'] += 1
    
    if CT['frame'] == 0:
        first_tc = CT['true_count']
        first_fc = CT['false_count']
    
    CT['frame'] += 1

    if CT['frame'] == 101:  # เปลี่ยนจาก 10 เป็น 11
        last_tc = CT['true_count']
        last_fc = CT['false_count']
        t_rate = last_tc - first_tc
        f_rate = last_fc - first_fc
        CT['frame'] = 0  # รีเซ็ต frame เป็น 0
    
    true_bar = '#' * int(t_rate/2)
    false_bar = '#' * int(f_rate/2)
     
    print(f"t_rate: {true_bar}  {t_rate} ")
    print(f"f_rate: {false_bar} {f_rate} ")
    print(f"called: {CT['called']}")




if __name__ == "__main__":
    #from udtablegame import udtg
    #b, m = udtg.flappy_bird(0)
    #while CT['called']!=100000:
        #key = ml(b, m)
        #b, m = udtg.flappy_bird(key)
        #udtg.show(b, m)
        #show_stats(m)
        #time.sleep(0)  # Adjusted sleep time for better readability
