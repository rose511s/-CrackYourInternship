#User function Template for python3

class Solution:
    def uniquePerms(self, arr, n):
        # code here 
         res=[]
         d={}
         def backtrack(i,ls):
             if i==n:
                 if not d.get(tuple(ls)):
                     res.append(ls.copy())
                     d[tuple(ls)]=True
                 return
             for j in range(i,n):
                 ls[i],ls[j]=ls[j],ls[i]
                 backtrack(i+1,arr)
                 ls[i],ls[j]=ls[j],ls[i]
         backtrack(0,arr)
         return sorted(res)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        res = ob.uniquePerms(arr,n)
        for i in range(len(res)):
            for j in range(n):
                print(res[i][j],end=" ")
            print()
# } Driver Code Ends
