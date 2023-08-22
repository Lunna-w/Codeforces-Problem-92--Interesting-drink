def binary_search(prices, x):
    
    l, r = 0, len(prices) - 1
    pos = -1
    while l <= r:
        mid = (l + r) // 2
        if prices[mid] <= x:
            pos = mid
            l = mid + 1
        else:
            r = mid - 1
    return pos + 1  

n = int(input())
prices = list(map(int, input().split()))
prices.sort()

q = int(input())
for _ in range(q):
    mi = int(input())
    print(binary_search(prices, mi))