def combine_lists(list1, list2):
    combined = sorted(list1 + list2, key=lambda x: x['positions'][0])
    result = []

    def is_more_than_half_overlap(a, b):
        
        left1, right1 = a['positions']
        left2, right2 = b['positions']
        overlap = max(0, min(right1, right2) - max(left1, left2))
        len1 = right1 - left1
        return overlap > (len1 / 2)

    i = 0
    while i < len(combined):
        curr = combined[i]
        j = i + 1
        while j < len(combined) and is_more_than_half_overlap(curr, combined[j]):
            curr['values'] += combined[j]['values']
            curr['positions'][1] = max(curr['positions'][1], combined[j]['positions'][1])
            j += 1
        result.append(curr)
        i = j

    return result

list1 = [{"positions": [2, 6], "values": ["A"]}]
list2 = [{"positions": [3, 8], "values": ["B"]}]
print(combine_lists(list1, list2))
