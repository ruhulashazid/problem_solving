# Input the number of elements in the set and the elements
n = int(input())
s = set(map(int, input().split()))

# Input the number of other sets
num_sets = int(input())

# Execute mutation operations on the set
for _ in range(num_sets):
    operation, length = input().split()
    other_set = set(map(int, input().split()))
    
    if operation == "intersection_update":
        s.intersection_update(other_set)
    elif operation == "update":
        s.update(other_set)
    elif operation == "symmetric_difference_update":
        s.symmetric_difference_update(other_set)
    elif operation == "difference_update":
        s.difference_update(other_set)

# Output the sum of elements in the set
print(sum(s))
