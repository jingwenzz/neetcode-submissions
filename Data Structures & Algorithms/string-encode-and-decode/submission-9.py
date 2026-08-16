class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        results = []
        i = 0
        while i < len(s):
            j = i + 1
            while s[j] != "#":
                j += 1
            length = int(s[i: j])
            word = s[j + 1: j + length + 1]
            results.append(word)
            i = j + 1 + length
    
        return results
