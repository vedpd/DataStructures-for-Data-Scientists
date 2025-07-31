class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups ={}

        for word in strs :
            sign = ''.join(sorted(word))

            if sign in anagram_groups:
                anagram_groups[sign].append(word)
            else:
                anagram_groups[sign] = [word]

        return list(anagram_groups.values())        