def second_half_rev(s):
    mid_str = len(s) // 2
    second_half = s[mid_str:]
    rev_str = second_half[::-1]
    return rev_str

print(second_half_rev("argentina"))
