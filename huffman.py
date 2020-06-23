'''source: https://gist.github.com/mreid/fdf6353ec39d050e972b'''

class huff:
    def __init__(self,p):

        self.code=self.huffman(p)

    def huffman(self,p):
        '''Return a Huffman code for an ensemble with distribution p.'''
        #print(sum(p.values()))
        #assert(sum(p.values()) == 1.0) # Ensure probabilities sum to 1

        # Base case of only two symbols, assign 0 or 1 arbitrarily
        if(len(p) == 2):
            return dict(zip(p.keys(), ['0', '1']))

        # Create a new distribution by merging lowest prob. pair
        p_prime = p.copy()
        a1, a2 = self.lowest_prob_pair(p)
        p1, p2 = p_prime.pop(a1), p_prime.pop(a2)
        p_prime[a1 + a2] = p1 + p2

        # Recurse and construct code on new distribution
        c = self.huffman(p_prime)
        ca1a2 = c.pop(a1 + a2)
        c[a1], c[a2] = ca1a2 + '0', ca1a2 + '1'

        return c

    def lowest_prob_pair(self,p):
        '''Return pair of symbols from distribution p with lowest probabilities.'''
        assert(len(p) >= 2) # Ensure there are at least 2 symbols in the dist.

        sorted_p = sorted(p.items(), key= lambda x: x[1])
        return sorted_p[0][0], sorted_p[1][0]


