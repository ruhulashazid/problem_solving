def simpleArraySum(ar):
    return sum(ar)

# Read input
n = int(input())


arr = list(map(int, input().split()))

result = simpleArraySum(arr)

print(result)