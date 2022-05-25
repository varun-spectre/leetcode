class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        start = 0
        end = 1
        d = {}
        d[s[start]] = start
        max_s = 1
        while(start <= len(s)-1):
            if end >= len(s):
                max_s = max(max_s, end-start)
                # print(start, end, s[start:end])
                break
            if s[end] in d.keys():
                # print(start, end, s[start:end])
                max_s = max(max_s, end-start)
                start += 1
                end = start+1
                if start >= len(s):
                    break
                else:
                    d = {}
                    d[s[start]] = start
            else:
                d[s[end]] = end
                end += 1
        return max_s