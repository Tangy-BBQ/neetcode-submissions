class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        min_window = ""
        min_len = 0
        
        t_freq_map = {}
        for i in range(len(t)):
            t_freq_map[t[i]] = t_freq_map.get(t[i], 0) + 1
        cur_freq_map = {}

        have = 0
        need = len(t_freq_map)

        start = 0
        for end in range(len(s)):
            char = s[end]
            cur_freq_map[char] = cur_freq_map.get(char, 0) + 1

            if char in t_freq_map and cur_freq_map[char] == t_freq_map[char]:
                have += 1

            while have == need:
                current_len = end - start + 1
                if min_len == 0 or current_len < min_len:
                    min_window = s[start:end+1]
                    min_len = len(min_window)
                
                left_char = s[start]
                cur_freq_map[left_char] -= 1
                
                if left_char in t_freq_map and cur_freq_map[left_char] < t_freq_map[left_char]:
                    have -= 1
                    
                start += 1
                
        return min_window