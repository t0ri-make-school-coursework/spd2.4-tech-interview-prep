def make_histogram(handle):
    histogram = {}
    for char in handle:
        if char not in histogram:
            histogram[char] = 1
        elif char in histogram:
            histogram[char] += 1

    return histogram


def suggest(target_handle, all_handles, handle_count):
    target_histogram = make_histogram(target_handle)
    all_histograms = {}
    
    for handle in all_handles:
        handle_clean = set(handle.lower())
        count = 0
        for char in handle_clean:
            if char in target_histogram:
                count += 1
            else:
                count -= 1

        if count in all_histograms:
            all_histograms[count].append(handle)
        else:
            all_histograms[count] = [handle]
        
    keys = all_histograms.keys()
    keys.sort(reverse=True)
    
    output = []
    index = 0
    while len(output) < handle_count:
        for handle in all_histograms[keys[index]]:
            output.append(handle)
        index += 1
    
    return output

handles = ['DogeCoin', 'YangGang2020', 'HodlForLife', 'fakeDonaldDrumpf', 'GodIsLove', 'BernieOrBust']
print(suggest('iLoveDogs', handles, 2))
