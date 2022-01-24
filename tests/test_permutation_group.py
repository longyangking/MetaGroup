import sys 
sys.path.append("..")

import numpy as np
from metagroup import PermutationGroup, Cycle, get_cycles_from_list, get_PermutationGroup_by_list

if __name__== "__main__":
    cycle = Cycle([[2,3],[1,6,7]])
    print(cycle.get_generator())

    cycle1 = Cycle([[2,3],[1,6,7]])
    cycle2 = Cycle([[1,2],[4,5]])
    cycle3 = Cycle([])
    group = PermutationGroup([cycle1, cycle2, cycle3])
    print(group.get_generator())


    cycle = get_cycles_from_list([6,3,2,4,5,7,1])
    print(cycle.get_generator())

    group = get_PermutationGroup_by_list([6,3,2,4,5,7,1])
    print(group.get_generator())