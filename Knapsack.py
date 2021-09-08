import math

def find_powerset(num_items, items):
    pow_set = [[]]
    for item in items:
        set = [new+[item] for new in pow_set]
        pow_set.extend(set)
    return pow_set


def exhaustive(powerset, weight_cap):
    knapsack = {}
    sol = 0
    for i, set in enumerate(powerset):
        set_val = 0
        set_wgt = 0
        for item in set:
            set_val += item[1]
            set_wgt += item[0]
        if set_wgt <= weight_cap and set_val > sol:
            sol = set_val
            knapsack = set
    return knapsack, sol


def heuristic(items, weight_cap):
    curr_weight = weight_cap
    knapsack = []
    sol = 0

    items.sort(key = lambda x: (float(x[1]/x[0]), x[1]), reverse = True)

    for item in items:
        if item[0] <= curr_weight:
            knapsack.append(item)
            sol += item[1]
            curr_weight -= item[0]
    return knapsack, sol


def start(file_name):   
    weight_cap = 0     # initalize vars. and lists
    uniq_items = 0
    weights = []
    values = []
    items = []

    with open(file_name, 'r') as file:  # open file
        for line in file:
            if weight_cap == 0: weight_cap = (int) (line); continue     # determine weight cap. & # unique items
            if uniq_items == 0: uniq_items = (int) (line); continue

            for i, var in enumerate(line.split()):          # create weight & value lists
                if i % 2 == 0: weights.append(int(var))
                if i % 2 != 0: values.append(int(var))
    
    for i in range(uniq_items):                             # combine lists
        items.append((weights[i], values[i]))

    powerset = find_powerset(uniq_items, items)             # call powerset function
    exh_set, exh_sol = exhaustive(powerset, weight_cap)     # call functions for both approaches
    heu_set, heu_sol = heuristic(items, weight_cap)

    print("Exh. Sol. : ", exh_sol, " ", exh_set)            # print solutions
    print("Heu. Sol. : ", heu_sol, " ", heu_set)

start('input2.txt')
start('input.txt')
start('input3.txt')