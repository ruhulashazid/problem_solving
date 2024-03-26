n_english = int(input()) # Input the number of students subscribed to English newspaper and their roll numbers
english_subscribers = set(map(int, input().split()))


n_french = int(input()) # Input the number of students subscribed to French newspaper and their roll numbers
french_subscribers = set(map(int, input().split()))

# Find students subscribed only to English newspaper
english_only_subscribers = english_subscribers.difference(french_subscribers)


print(len(english_only_subscribers)) # Output the total number of students who are subscribed to English newspaper only
