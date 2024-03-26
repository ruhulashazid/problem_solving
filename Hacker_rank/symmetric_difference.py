n_english = int(input()) # Input the number of students subscribed to English newspaper and their roll numbers
english_subscribers = set(map(int, input().split()))


n_french = int(input()) # Input the number of students subscribed to French newspaper and their roll numbers
french_subscribers = set(map(int, input().split()))

# Find students subscribed either to English or French newspaper but not both
subscribers_not_both = english_subscribers.symmetric_difference(french_subscribers)

# Output the total number of students who have subscribed to either English or French newspaper but not both
print(len(subscribers_not_both))
