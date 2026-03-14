class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map={}
        if len(s)!=len(t):
            return False
        for c in s:
            hash_map[c]=hash_map.get(c,0)+1
        for ch in t:
            if ch not in hash_map:
                return False
            hash_map[ch]-=1
            if hash_map[ch]<0:
                return False
        return True

        