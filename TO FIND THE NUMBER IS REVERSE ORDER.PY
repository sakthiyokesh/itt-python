	TO FIND THE NUMBER IS REVERSE ORDER


n=int(input("Enter the number:"))
r=t=0
s=n
if 1<= n <= 100000:
   while s!=0:
      r=s%10
      t=(t*10)+r
      s=s//10
   print(t)
else:
   print("INVALID NUMBER")