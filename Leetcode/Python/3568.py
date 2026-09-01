class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        ROWS = len(classroom)
        COLS = len(classroom[0])
        
        start = None
        l_cells = []
        
        for r in range(ROWS):
            for c in range(COLS):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    l_cells.append((r, c))
                    
        if not l_cells:
            return 0
            
        num_L = len(l_cells)
        l_idx = {cell: i for i, cell in enumerate(l_cells)}
        target_mask = (1 << num_L) - 1
        
        dq = deque([(start[0], start[1], 0, energy, 0)])
        
        visited = {(start[0], start[1], 0): energy}
        
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        while dq:
            r, c, mask, cur_energy, moves = dq.popleft()
            
            if mask == target_mask:
                return moves
                
            if cur_energy == 0:
                continue
                
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < ROWS and 0 <= nc < COLS and classroom[nr][nc] != 'X':
                    n_energy = cur_energy - 1
                    
                    if n_energy < 0:
                        continue
                        
                    if classroom[nr][nc] == 'R':
                        n_energy = energy
                        
                    n_mask = mask
                    if classroom[nr][nc] == 'L':
                        n_mask |= (1 << l_idx[(nr, nc)])
                        
                    if n_mask == target_mask:
                        return moves + 1
                        
                    if n_energy > visited.get((nr, nc, n_mask), -1):
                        visited[(nr, nc, n_mask)] = n_energy
                        dq.append((nr, nc, n_mask, n_energy, moves + 1))
                        
        return -1
