def quick_sort(s):
    if len(s)<=1:
        return s
    base = s[0]
    left = list(filter(lambda x: x<base, s))
    right = list(filter(lambda x: x>base, s))
    center = [i for i in s if i==base]
    return quick_sort(left) + center + quick_sort(right)