import numpy as np
import math
from huffman import *
from scipy.stats import bernoulli

def poweroftwo(x):
    return math.ceil(math.log(x, 2)) == math.floor(math.log(x, 2))


class comp:

    def __init__(self, m, items):
        self.m = m
        self.items = items
        self.test = self.algo(self.items)

    def algo(self, totest):
        count = 0
        remaining = totest
        positive=[]
        while (len(remaining) >= self.m):
            #print(remaining)

            count+=1
            B = remaining[:self.m]
            #tested=[]
            remaining = remaining[self.m:]
            if 1 in [patient[0] for patient in B]:
                if poweroftwo(self.m):
                    tmp=self.binary_split(B)
                    for i in B:
                        if i in tmp[0]:
                            continue
                        else:
                            remaining.append(i)
                    count+=tmp[1]
                    positive.extend(tmp[2])
                else:
                    tmp=self.m_ary_split(B)
                    for i in B:
                        if i in tmp[0]:
                            continue
                        else:
                            remaining.append(i)
                    count+=tmp[1]
                    positive.append(tmp[2])

            else:
                continue
        #print(remaining)
        #print(B)
        for i in remaining:
            if i[0]==1:
                positive.append(i)
        count += len(remaining)
        return count

    def binary_split(self, B):
        count = 0
        tested=[]
        while (len(B) != 1):
            count += 1
            C = B[: int(len(B)/2)]

            if 1 in [patient[0] for patient in C]:
                B = C
            else:
                tested.extend(C)
                B = B[int(len(B) / 2):]
        tested.extend(B)
        return tested, count, B

    def m_ary_split(self, B):
        p=self.gen_p(B)
        samples=p.copy()
        count=0
        tested=[]
        k=0
        totest=[]
        topop=[]
        while(1):
            if len(samples) == 1:
                for i in samples:
                    positive=i
                tested.append(positive)
                return tested, count, positive
            for i in samples:
                if samples[i][k]=='0':
                    totest.append(i)
            if 1 in [patient[0] for patient in totest]:
                count+=1
                for j in samples:
                    if j not in totest:
                        topop.append(j)
                for j in topop:
                    samples.pop(j)
            else:
                tested.extend(totest)
                count+=1
                for j in samples:
                    if j in totest:
                        topop.append(j)
                for j in topop:
                    samples.pop(j)
            topop=[]
            k+=1
            totest=[]




    def gen_p(self,p):
        odds=1/len(p)
        dist={}
        for i in p:
            dist[i]=odds
        result=huff(dist).code
        return result


# test=[]
# p=.05
# dist=bernoulli(p)
# population=dist.rvs(size=100)
# id=0
# for i in population:
#     test.append((i,id))
#     id+=1
#
#
# test_comp=comp(10,test)
# print(population)
# print(test_comp.test)
#
# print(np.count_nonzero(population==1)==len(test_comp.test[1]))