class Solution:
    def distinctSubseqII(self, s: str) -> int:
        mod = 10**9 +7
        n=len(s)
        s=list(s)
        last = [-1]*26
        dp = [0]*(n+1)
        dp[0]=1
        for i in range(1,n+1):
            dp[i] = (2 * dp[i-1])%mod
            idx = ord(s[i-1]) - ord('a')
            if last[idx]!=-1:
                dp[i] = (dp[i]-dp[last[idx]])
            last[idx] = i-1
        return (dp[n]-1+mod)%mod