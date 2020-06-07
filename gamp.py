import numpy as np


class gamp:

    def __init__(self, ro, p1, p2, y, A, mode=0, iter=1000, threshold=1e-3):
        """ Algorithm mode: 0 corresponds to max number of iteration/
        1 corresponds to error improvement threshold,
         percentage of sick patients ρ,
         false negative probability p1, false positive probability p2,
        measurements y, and matrix A."""
        self.ro=ro
        self.p1=p1
        self.p2=p2
        self.y=y
        self.A=A
        self.mode = mode
        self.iter = iter
        self.threshold = threshold
        self.fit()

    def fit(self):
        s=0
        k=0
        h=0
        N=np.shape(self.A)[1]
        M=np.shape(self.A)[0]

        if self.mode:

        else:
            for i in range(self.iter):
                theta=np.matmul(self.A,self.A)*s
