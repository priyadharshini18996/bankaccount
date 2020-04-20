def diagonalDifference(arr):
    
    primary_diagonal = 0
    secondary_diagonal=0
    length = len(arr[0])
    for count in range(length):
        primary_diagonal += arr[count][count]
        secondary_diagonal += arr[count][(length-count-1)]
    return abs(primary_diagonal-secondary_diagonal)
    print (abs(primary_diagonal-secondary_diagonal))


n = int(input('enter the num of row and column:').strip())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr)
print("diagonal difference is:",str(result))
