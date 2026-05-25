class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ## we know length of s1, 

        ## frequency array, fixed length 26

        if len(s1) > len(s2):
            return False

        freqS1 = [0] * 26
        freqS2 = [0] * 26

        for i in range(len(s1)):
            freqS1[ord(s1[i]) - ord('a')] += 1
            freqS2[ord(s2[i]) - ord('a')] += 1

        start = 0
        for end in range(len(s1), len(s2)):
            
            ## check through frequency array if current window is a permuation of s1
            if freqS2 == freqS1:
                return True
            

            freqS2[ord(s2[start]) - ord('a')] -= 1
            start += 1
            freqS2[ord(s2[end]) - ord('a')] += 1
        

        return freqS2 == freqS1
        


