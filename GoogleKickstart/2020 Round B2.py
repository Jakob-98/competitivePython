T = int(input())
for case in range(T):
    N, D = map(int, input().split())
    B = list(map(int, input().split()))
    nd = D
    while B:
        last = B.pop()
        while True:
            if nd%last == 0:
                break
            else:
                nd -= 1
    print('Case #' + str(case+1) + ": " + str(nd)) 
