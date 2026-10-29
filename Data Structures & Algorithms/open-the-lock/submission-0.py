class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        if '0000' in visited:
            return -1

        q = deque(['0000'])
        visited.add('0000')
        numTurns = 0

        while q:
            for _ in range(len(q)):   
                curr = q.popleft()

                if curr == target:
                    return numTurns

                for i in range(4):
                    for direction in (-1, 1):
                        digit = (int(curr[i]) + direction) % 10
                        nxt = curr[:i] + str(digit) + curr[i+1:]
                        if nxt not in visited:
                            visited.add(nxt)
                            q.append(nxt)

            numTurns += 1

        return -1



