from comp import *
import matplotlib.pyplot as plt

iter=20
pop_size=1000
preva=0.4

M=[2,4,5,6,10]

P=np.arange(0,preva,0.01)
for m in M:
    print(m)
    tests=[]
    for p in P:
        curr_test=0

        for i in range(iter):
            curr_pop=[]
            dist=bernoulli(p)
            population=dist.rvs(size=pop_size)
            id=0
            for i in population:
                curr_pop.append((i,id))
                id+=1
            iter_comp=comp(m,curr_pop)
            curr_test+=iter_comp.test

        tests.append(curr_test/iter)
    plt.plot(P,tests,label=('m= '+str(m)))
plt.legend()
plt.show()