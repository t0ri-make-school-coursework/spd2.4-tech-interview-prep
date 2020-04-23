# Given an array a of n numbers and a count k, find the k largest values in the array a.
# Example: a=[5, 1, 3, 6, 8, 2, 4, 7], k=3 => [6, 8, 7]

def largest_value_built_in(items, k):
    # Built-in Timsort - O(n log n)
    items.sort()
    return items[-k:]
    

def largest_value_brute(items, k):
    # Bubble Sort - O(n^2)
    if len(items) is 0:
          return items
      
    for i in range(len(items)):
        for j in range(len(items) - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    
    return items[-k:]


if __name__ == "__main__":
    print(largest_value_built_in([5, 1, 3, 6, 8, 2, 4, 7], 3))
    print(largest_value_brute([5, 1, 3, 6, 8, 2, 4, 7], 3))
