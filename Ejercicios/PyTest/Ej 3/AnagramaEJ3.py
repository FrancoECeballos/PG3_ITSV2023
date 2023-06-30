class Anagrama():
    def is_anagram(self,word1,word2):
        sort1 = [word1[i] for i in range(0,len(word1))]
        sort1.sort()
        sort2 = [word2[i] for i in range(0,len(word2))]
        sort2.sort()

        if sort1 == sort2:
            return True
        else:
            return False
        
        