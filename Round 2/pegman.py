# Copyright (c) 2015 kamyu. All rights reserved.
#
# Google Code Jam 2015 Round 2 - Problem A. Pegman
# https://code.google.com/codejam/contest/8234486/dashboard#s=p0
#
# Time:  O(R * C)
# Space: O(R + C)
#

def pegman():
    R, C = map(int, raw_input().strip().split())
    grid = [raw_input().strip() for _ in xrange(R)]
    
    # Find each left-, right-, up-, and down-most in each row and column.
    row_left = [min([j for j in xrange(C) if grid[i][j] != "."]+[C]) for i in xrange(R)]
    row_right = [max([j for j in xrange(C) if grid[i][j] != "."]+[-1]) for i in xrange(R)]
    col_up = [min([i for i in xrange(R) if grid[i][j] != "."]+[R]) for j in xrange(C)]
    col_down = [max([i for i in xrange(R) if grid[i][j] != "."]+[-1]) for j in xrange(C)]
    
    ans, impossible = 0, False
    for i in xrange(R):
        if impossible:
            break
        for j in xrange(C):
            if grid[i][j] == ".":
                continue
            else:
                can_left = row_left[i] < j
                can_right = row_right[i] > j
                can_up = col_up[j] < i
                can_down = col_down[j] > i
                
                # Impossible if each direction is
                if not (can_left or can_right or can_up or can_down):
                    impossible = True
                    break
                if (can_left and grid[i][j] == "<") or \
                   (can_right and grid[i][j] == ">") or \
                   (can_up and grid[i][j] == "^") or \
                   (can_down and grid[i][j] == "v"):
                    continue
                else: # Change the direction.
                    ans += 1
    if impossible:
        return "IMPOSSIBLE"
    else:
        return ans

for case in xrange(input()):
    print "Case #%d: %s" % (case+1, pegman())
