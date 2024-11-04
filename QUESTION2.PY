#Create a function that checks whether a given number is prime or not. Return True if it's prime, otherwise False 
num=int(input("ENTER A NUMBER"))
def prime(num):
    if num<=1:
      return False
    if num in range(2,int(num**0.5)+1):
        if num%num==0:
         return True
    if num%2==0 or num%3==0:
        return False
if prime(num):
       print(num,"is a prime number")
else:
   print(num,"is not a prime number")




