cases = int(input())
for case in cases:
    N = int(input())
    heights = list(map(int, input().split()))
    peaks = 0
    for i in range(1,len(heights)-1):
        if heights[i] > heights[i+1] and heights[i] > heights[i-1]:
            peaks += 1
    print('Case #' + str(case) + ": " + str(peaks))
