next_level = [root]
current_level = []

even = True
even_sum = 0
odd_sum = 0
while next_level:
    current_level = next_level
    next_level = []
    max_val = 0
    for ele in current_level:
        if ele.val > max_val:
            max_val = ele.val
        if ele.left:
            next_level.append(left)
        if ele.right:
            next_level.append(right)
    if even:
        even_sum += max_val
    else:
        odd_sum += max_val

return max(even_sum, odd_sum)
