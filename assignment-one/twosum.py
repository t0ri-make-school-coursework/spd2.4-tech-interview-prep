# Given an array a of n numbers and a target value t, find two numbers whose sum is t.
# Example: a=[5, 3, 6, 8, 2, 4, 7], t=10 => [3, 7] or [6, 4] or [8, 2]

def two_sum_brute_force(items, t):
    # loop through same list twice
    # to compare values to one another
    for item1 in items:
        for item2 in items:
            if item1 + item2 is t: # if target is met
                return [item1, item2]  # return pairs
    
    return False # if no combination meets target


def two_sum_dictionary(items, t):
    numbers = dict()

    for item in items:
        complement = t - item # get complement
        # if item is in dictionary, 
        # return the pair of values
        if item in numbers:
            return [item, complement]
        
        # if not, add it to dictionary
        numbers[complement] = item
    
    return False # if no combination meets target


if __name__ == "__main__":
    print(two_sum_brute_force([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8))
    print(two_sum_dictionary([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4))
