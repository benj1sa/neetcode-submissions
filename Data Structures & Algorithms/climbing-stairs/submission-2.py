class Solution:
    def climbStairs(self, n: int) -> int:

        def help(n, nmap):
            if n <= 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n in nmap:
                return nmap[n]
            nmap[n] = help(n - 1, nmap) + help(n - 2, nmap)
            return nmap[n]
        
        nmap = {}
        return help(n, nmap)