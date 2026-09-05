class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        seen = set()

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in seen:
                    count += 1
                    stack = [(r,c)]

                    while stack:
                        i,j = stack.pop()

                        if (i,j) in seen:
                            continue
                        seen.add((i,j))
                        for di, dj in ((1,0), (-1,0), (0,1), (0,-1)):
                            ni, nj = i + di, j + dj

                            if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == "1":
                                stack.append((ni,nj))

        return count