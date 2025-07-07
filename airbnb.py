#http://www.meeplemountain.com/wp-content/uploads/2017/05/scoring-example-1.jpg
from collections import deque

grid = [

  "W0 W0 F0 F0 F0",
  "W0 W1 F0 S2 S1",
  "G0 X0 G1 G0",
  "S0 M2 M0 G1 F0"
]
# Return total points
# come to hole later
# sum (C * Crowns on a color)

def total(raw_grid):
    # clean up grid
        
    if len(raw_grid) == 0: 
        return 0
        
    grid = []

    for row in raw_grid: 
        grid.append([(item[0], int(item[1])) for item in row.split(" ")])\
    
    ROWS = len(grid)
    COLS = len(grid[0])
    visited = set()
    
    def get_neigh(coord): 
        deltas = [(0,1), (0, -1), (1,0), (-1, 0)]
        color = grid[coord[0]][coord[1]][0]
        res = []
        for delta in deltas: 
            i = coord[0] + delta[0]
            j = coord[1] + delta[1]
            
            if 0 <= i < ROWS and 0 <= j < len(grid[i]) and color == grid[i][j][0]: 
                res.append((i, j))
            
        print(f"Neigh {res} for {coord}")
        return res
    
    def bfs(root): 
        # returns (cells * crowns)
        
        q = deque([root])
        visited.add(root)
        
        cell_count = 0
        crown_count = 0
        while q: 
            cur = q.popleft()
            
            cell_count += 1 
            print(f"{cur[0]}, {cur[1]}")
            crown_count += grid[cur[0]][cur[1]][1] 
            for n in get_neigh(cur): 
                if n not in visited: 
                    print(f"Neigh filtered {n}")
                    visited.add(n)
                    q.append(n)
                    
        # print(f"Cells={cell_count}, CR={crown_count}")
        return cell_count * crown_count
        
        
    # do bfs over each color
    val = 0
    for i in range(ROWS): 
        for j in range(row): # I don't know why i kept row here
        for j in range(len(grid[i])): 
            if (i, j) not in visited: 
                # print(f"BFS @ ({i},{j} = {grid[i][j]})")
                val += bfs((i,j))
                
    return val
            
        
# total = 41
if __name__ == "__main__": 
    print(total(grid))
