import random
class maze:
    def __init__(self,a,ld,ins,fs):
        self.a = a
        self.s = a
        self.l = []
        self.ld = ld
        self.lr = 0.1
        self.gamma = 0.6
        self.q = []
        self.ins = ins
        self.fs = fs
    def new_s(self,s,a):
        return a
    def calc(self,s,a):
        lr,gamma = self.lr,self.gamma
        return ((1-lr)*self.q[s][a] + lr*(self.l[s][a]+gamma*max(self.q[maze.new_s(self,s,a)])))

    def train(self,ins,fs):
        self.l = [[-1 for i in range(self.a)] for j in range(self.a)]
        for i in range(self.a):
            for j in range(self.a):
                if j in self.ld[i]:
                    self.l[i][j] = 0.1
                    if j ==  fs :
                        self.l[i][j] =1
        self.q =[[0 for i in range(self.a)] for j in range(self.s)]
        steps,num = self.a*100,self.a*100
        eps = 0.05
        for i in range(num):
            csd = random.randint(0,self.s-1)
            for j in range(steps):
                cs = csd
                epsd = random.random()
                if cs == fs:
                    break
                if epsd > eps:
                    self.q[cs][self.q[cs].index(max(self.q[cs]))] = maze.calc(self,cs,self.q[cs].index(max(self.q[cs])))
                    cs = maze.new_s(self,cs,self.q[cs].index(max(self.q[cs])))
                else:
                    x = random.randint(0,self.a-1)
                    self.q[cs][x] = maze.calc(self,cs,x)
                    cs = maze.new_s(self,cs,x)
        cs = ins
        ans = []
#        print('..')
        while 1 :
            ans.append(cs)
            cs = self.q[cs].index(max(self.q[cs]))
            if cs == fs:
                break
        ans.append(fs)
        return ans

    def main(self):
        return (self.train(self.ins,self.fs))

