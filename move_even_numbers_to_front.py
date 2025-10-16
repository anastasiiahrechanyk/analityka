def sort_array_by_parity(nums):
    if not nums:
        return []
    
    head, *tail = nums
    
    tail_sorted = sort_array_by_parity(tail)
    
    if head % 2 == 0:
        return [head] + tail_sorted
    else:
        even_part = [x for x in tail_sorted if x % 2 == 0]
        odd_part = [x for x in tail_sorted if x % 2 != 0]
        return even_part + [head] + odd_part
