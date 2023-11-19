def combinations(n, r):
    if r == 0 or r == n:
        return 1
    else:
        return combinations(n - 1, r - 1) + combinations(n - 1, r)