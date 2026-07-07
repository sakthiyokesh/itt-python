class Solution:
    def numSpecialEquivGroups(self, words: list[str]) -> int:
       
        signatures = set()
        
        for word in words:
          
            even_chars = sorted(word[0::2])
            
            
            odd_chars = sorted(word[1::2])
            
          
            signature = (tuple(even_chars), tuple(odd_chars))
            
          
            signatures.add(signature)
            
       
        return len(signatures)

        
