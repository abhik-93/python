def subArraySum(arr, n, s) -> list[int]:
    for i in range(n):
        sum1 = arr[i]
        found = False
        for j in range(i, n):
            sum1 += arr[j]
            if sum1 > s:
                break
            if sum1 == s:
                print(i + 1, j + 1)
                found = True
                break
        if found:
            break


subArraySum([1, 2, 3, 7, 5], 5, 10)
# subArraySum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 15)
