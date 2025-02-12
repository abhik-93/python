class Solution:
    def findSubArrays(self, arr, n):
        hashMap = {}
        final_out = []
        out = 0
        sum1 = 0
        for i in range(n):
            sum1 += arr[i]
            if sum1 == 0:
                final_out.append((0,i))
                out += 1
            al = []
            if sum1 in hashMap:
                al = hashMap.get(sum1)
                for it in range(len(al)):
                    final_out.append((it+1, i))
                    out += 1
            al.append(i)
            hashMap[sum1] = al
        return out


# Driver Code
if __name__ == '__main__':
    arr = [6, 3, -1, -3, 4, -2,
           2, 4, 6, -12, -7]
    n = len(arr)
    ob = Solution()
    print(ob.findSubArrays(arr, n))
