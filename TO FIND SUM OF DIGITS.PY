	TO FIND SUM OF DIGITS


n=int(input("Enter the number:"))
r=t=0
s=n
if 1<= n <= 100000:
   while s!=0:
      r=s%10
      t=t+r
      s=s//10
   print(t)