from random import choice

class Distribution():
    def __init__(self,dim):
        self.dim = dim
        self.steps = [-1,0,1]
        self.pos = self.dim*[0]

    def _rv(self):
        step = 0
        i = -1
        vec = self.dim * [0]
        while step == 0:
            i+=1
            i = i%self.dim
            step = choice(self.steps)
        vec[i] = step
        return vec

    def _vec_add(self, v1,v2):
        if len(v1) < len(v2): mini = len(v1)
        else: mini = len(v2)

        res = []

        for i in range(0,len(v1)):
            res.append(v1[i] + v2[i])
        
        return res
    
    def update_pos(self):
        v = self._rv()
        self.pos = self._vec_add(self.pos,v)
