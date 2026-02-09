from collections import defaultdict


#CREATING EMPTY dict
norm_dict  = dict()
norm_dict2 = {}

print(type(norm_dict))
print(type(norm_dict2))

# CREATING EMPTY deafultDict
temp_dict = defaultdict(int)  # MANDATORY PASS CALLABLE OR NONE

"""
defaultdict(int)    # int() → 0
defaultdict(list)   # list() → []
defaultdict(set)    # set() → set()
defaultdict(dict)   # dict() → {}

                    note -> Callable can also be a lamda or user Defined Function
"""
print(type(temp_dict))

"""
    Counting Using Default Dict
"""