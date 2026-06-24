class Solution:

    def encode(self, strs: List[str]) -> str:
        # result = ""
        # for word in strs:
        #     result += str(len(word)) + "!" + word
        # return result
        return "".join(f"{len(s)}!{s}" for s in strs)


    def decode(self, s: str) -> List[str]:
        i, n = 0, len(s)
        arr = []
        while (i < n):
            start = i
            while(s[i] != '!'):
                i += 1
            word_len = int(s[start:i])
            i += 1
            arr.append(str(s[(i):(i+word_len)]))
            i += word_len
        return arr

