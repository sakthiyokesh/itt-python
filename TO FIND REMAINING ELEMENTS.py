	TO FIND REMAINING ELEMENTS

n=eval(input("Enter the number:"))
a=int(input("Enter the key:"))
l=len(n)
s=0
print("[",end="")
for i in range(l):
   if n[i]!=a:
      s=s+1;
      print(n[i],end=",")
   else:
      continue
for j in range(l-s):
   print ("_",end=",")
print ("j\n","no of remaining elements:",s)