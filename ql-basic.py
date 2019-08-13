import random
def new_s(s,a):
    return a
def calc(s,a):
    global q,lr,gamma,l
    return ((1-lr)*q[s][a] + lr*(l[s][a]+gamma*max(q[new_s(s,a)])))

def train(ins,fs):
    global ld,a,q,l,s
    l = [[-1 for i in range(a)] for j in range(a)]
    for i in range(a):
        for j in range(a):
            if j in ld[i]:
                l[i][j] = 0.0
                if j ==  fs :
                    l[i][j] =1
    q =[[0 for i in range(a)] for j in range(s)]
    
    steps,num = 1000,1000
    eps = 0.05
    for i in range(num):
        csd = random.randint(0,s-1)
        for j in range(steps):
            cs = csd
            epsd = random.random()
            if cs == fs:
                break
            if epsd > eps:
                q[cs][q[cs].index(max(q[cs]))] = calc(cs,q[cs].index(max(q[cs])))
                cs = new_s(cs,q[cs].index(max(q[cs])))
            else:
                x = random.randint(0,a-1)
                q[cs][x] = calc(cs,x)
                cs = new_s(cs,x)
    cs = ins
    while 1 :
        print(cs,end='-')
        cs = q[cs].index(max(q[cs]))
        if cs == fs:
            break

def main():
    global a,q,lr,gamma,l,ld,s
    s = int(input("Enter the number of rooms:"))
    a = s
    ld = []
    l = []
    for i in range(a):
        print('Enter the rooms connected to room ',i,':',end='')
        ld.append(list(map(int,input().split(','))))
    ins = int(input('Enter Initial state:'))

    routed = list(map(int,input('Enter the intermediate rooms and the final room:').split(',')))
    route = [ins]
    route.extend(routed)
    
    print('The route to be taken is :',end='')
    for i in range(len(route)-1):
        train(route[i],route[i+1])
    print(route[-1])
a = 0
s = 0
q = []
lr = 0.1
gamma = 0.6
l =[]
ld =[]
main()

