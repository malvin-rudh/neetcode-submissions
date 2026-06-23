class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
            Brute Force:
                Sort each of the strings --> O(m * n log n)
                group them using a hashmap where key is the sorted string and value 
                is the frequency of the sorted string
            
            More efficient approach:
                Since all are lowercase letters, and we have only 26 different lower
                case letters, we can use an array of size 26 as the keys of a hashmap
                since anagrams only care about the frequency of the letters
        """

        hashmap = {}

        for word in strs:
            count = [0] * 26
            for letter in word:
                index = ord(letter) - ord('a')
                count[index] += 1
            key = tuple(count)
            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(word)
        output = []
        for value in hashmap.values():
            output.append(value)
        
        return output


