class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            key = [0] * 26

            for char in word:
                key[ord(char) - ord('a')] += 1

            tuple_key = tuple(key)

            if tuple_key not in groups:
                groups[tuple_key] = []

            groups[tuple_key].append(word)

        return list(groups.values())