import itertools

k,m = map(int,input().split())

L = [list(map(int, input().split()))[1:] for i in range(k)]

result = 0
for i in itertools.product(*L):
    r = 0
    for n in i:
        r += n**2
        
    if result < r % m:
        result = r % m
print(result)

"""
PS D:\problem_solving\Hacker_rank\python_basic> cd "d:\problem_solving\Hacker_rank\python_basic"    
PS D:\problem_solving\Hacker_rank\python_basic> python -u "d:\problem_solving\Hacker_rank\python_basic\Maximize_It.py"
3 1000
2 5 4        
3 7 8 9      
5 5 7 8 9 10 
206
PS D:\problem_solving\Hacker_rank\python_basic> 

"""