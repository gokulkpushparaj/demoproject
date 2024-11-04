# Write a lambda function to check if a given string is a palindrome
def palindrome(k):
    return k==k[::-1]

k=(input("enter a word"))
answer= palindrome(k)

if answer:
    print("yes")

else:
    print("no")