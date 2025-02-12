class Solution:
    def remove_duplicate(self, A, N):
        n = 0
        for i in range(len(A)):
            if i == 0 or A[i] != A[i - 1]:
                A[n] = A[i]
                n += 1
        return n

#{
#  Driver Code Starts
#Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        n = Solution().remove_duplicate(arr, n)
        for i in range(n):
            print (arr[i], end=" ")
        print()


# } Driver Code Ends