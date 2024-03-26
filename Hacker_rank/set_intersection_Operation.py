'''
n = int(input())
english = set( map( int, input().split() ) )

p = int(input())
franch = set( map( int, input().split() ) )
new_set = english.intersection(franch)
print( len(new_set) )

'''
# Input the number of students subscribed to English newspaper and their roll numbers
n_english = int(input())
english_subscribers = set(map(int, input().split()))

# Input the number of students subscribed to French newspaper and their roll numbers
n_french = int(input())
french_subscribers = set(map(int, input().split()))

# Find the common subscribers
common_subscribers = english_subscribers.intersection(french_subscribers)

# Output the total number of students who have subscribed to both newspapers
print(len(common_subscribers))

'''
Sample Input

9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8

Sample Output

5
'''


