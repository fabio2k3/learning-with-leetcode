from collections import deque

class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        indegree = [[0] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < cols:
                        if matrix[nr][nc] < matrix[r][c]:
                            indegree[r][c] += 1

        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if indegree[r][c] == 0:
                    queue.append((r, c))

        distance = [[1] * cols for _ in range(rows)]

        result = 1

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if matrix[nr][nc] > matrix[r][c]:

                        distance[nr][nc] = max(
                            distance[nr][nc],
                            distance[r][c] + 1
                        )

                        result = max(result, distance[nr][nc])

                        indegree[nr][nc] -= 1

                        if indegree[nr][nc] == 0:
                            queue.append((nr, nc))

        return result