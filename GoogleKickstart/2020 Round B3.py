def parse_move(mv):
    for i, char in enumerate(mv):
        if char.isnumeric():
            depth = 0
            g = 0
            for j in range(i, len(mv)):
                if mv[j] == '(':
                    depth += 1
                if depth == 1 and mv[j] == ')':
                    g = j
                    break
                elif mv[j] == ')':
                    depth -= 1

            mv = mv[:i] + mv[g + 1:] + int(char)*mv[i+2:g]
            return mv
    return mv

cases = int(input())
for case in range(cases):
    pos = (1,1)
    mv = input()
    while "(" in mv:
        mv = parse_move(mv)
    moves = ['N', "E", "S," "W"]
    d = {move: mv.count(move) for move in mv}
    y = - d.get('N', 0) + d.get("S", 0)
    x = - d.get('W',0) + d.get("E", 0)
    ypos = (y) % (10 ** 9) + 1
    xpos = (x) % (10 ** 9) + 1
    print('Case #' + str(case+1) + ": " + str(xpos) + " " + str(ypos)) 
