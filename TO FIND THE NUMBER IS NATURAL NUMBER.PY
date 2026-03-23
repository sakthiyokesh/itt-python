	TO FIND THE NUMBER IS NATURAL NUMBER

n=int(input("Enter the numbers:"))
s=0
if 1<=n<=10000:
   for i in range(n+1):
      s+=i
   print ("sum of n series is",s)
else:
   print(" given input is out of range")