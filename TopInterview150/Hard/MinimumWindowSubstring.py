class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        window = {}
        required = len(need)      
        formed = 0                

        positions = []           
        head = 0                

        best_len = float('inf')
        best_start = 0

        p2 = 0
        while p2 < len(s):
            ch = s[p2]

            if ch in need:
                positions.append(p2)          
                window[ch] = window.get(ch, 0) + 1

                if window[ch] == need[ch]:
                    formed += 1

                while formed == required and head < len(positions):
                    left_pos = positions[head]
                    curr_len = p2 - left_pos + 1

                    if curr_len < best_len:
                        best_len = curr_len
                        best_start = left_pos

                    left_ch = s[left_pos]
                    window[left_ch] -= 1
                    if window[left_ch] < need[left_ch]:
                        formed -= 1

                    head += 1

            p2 += 1

        if best_len == float('inf'):
            return ""
        else:
            return s[best_start:best_start + best_len]