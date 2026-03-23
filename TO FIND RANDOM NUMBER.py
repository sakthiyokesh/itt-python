	TO FIND RANDOM NUMBER

a=eval(input("Enter the number:"))
n.sort()
l=len(n)
for  i in range(l):
   if (n[i]==0):
      print ("red",end=",")
   elif (n[i]==1):
      print ("blue",end= ",")
   elif(n[i]==2):
      print("green",end=",")