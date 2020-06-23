import numpy as np
from huffman import *

class gamp:

    def __init__(self, ro, p1, p2, y, A, mode=0, iter=1000, threshold=1e-3):
        """ Algorithm mode: 0 corresponds to max number of iteration/
        1 corresponds to error improvement threshold,
         percentage of sick patients ρ,
         false negative probability p1, false positive probability p2,
        measurements y, and matrix A."""
        self.ro = ro
        self.p1 = p1
        self.p2 = p2
        self.y = y
        self.A = A
        self.mode = mode
        self.iter = iter
        self.threshold = threshold
        self.fit()

    def fit(self):
        N = np.shape(self.A)[1]
        M = np.shape(self.A)[0]

        # Initializing parameters
        s = np.zeros(N, 1)
        k = np.zeros(M, 1)
        x_hat = np.zeros(N, 1)
        theta=np.matmul(np.matmul(self.A,self.A.transpose()),s)
        h = np.zeros(M, 1)

        all_h=[]
        all_s=[]
        all_xh=[]

        if self.mode:
            print("Threshold not implemented")
        else:
            for i in range(self.iter):
                theta = np.matmul(self.A, self.A) * s
