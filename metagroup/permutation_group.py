import numpy as np

class PermutationGroup:
    def __init__(self, cycles):
        self.cycles = cycles

    def cannonicalize(self):
        pass

    def get_elements(self):
        pass

    @property
    def order(self):
        ## Schreier–Sims algorithm
        return 0

    def coset(self, H):
        ## Todd–Coxeter algorithm and Knuth–Bendix algorithm
        pass

    def random_element(self):
        # Product-replacement algorithm 
        pass

    @property
    def subgroup(self): 
        # get all subgroups
        pass

    @property
    def quotinent(self, H):
        # get the quotient group G/H
        pass

    @property
    def product(self, H):
        # get the direct product G X H
        pass

    def get_isomorphic(self):
        pass