
class Solution:
    def numberOfWays(self, s: str, t: str, k: int) -> int:
        n=len(t)
        x=s+s[:n-1]
        MOD=10**9+7

        def kmp():
            count=0
            lps=[0]*n
            i,j=1,0
            while i < n:
                if t[i] == t[j]:
                    j+=1
                    lps[i]=j
                    i+=1
                elif j > 0:
                    j=lps[j-1]
                else:
                    i+=1
            
            i,j=0,0
            while i < len(x):
                if x[i] == t[j]:
                    j+=1
                    i+=1
                elif j > 0:
                    j=lps[j-1]
                else:
                    i+=1
                if j == n:
                    count+=1
                    j=lps[j-1]
            return count
        
        good=kmp()
        bad,same=n-good,int(s == t)

        if good == 0:
            return 0
        
        dp=[same,1-same] # [good ways, bad ways]
        # after each move i have to rotate cant stay on same rotation
        for _ in range(k):
            newdp=[0,0]
            newdp[0]=(dp[0]*(good-1) + dp[1]*(good))%MOD
            # good to other goods  +  bad to good
            newdp[1]=(dp[0]*(bad) + dp[1]*(bad-1)) %MOD
            # good to bad  +  bad to other bads
            dp=newdp

        return dp[0]
