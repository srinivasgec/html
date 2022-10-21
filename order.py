a=int(input("Enter the value :: "))
b=int(input("Enter the value :: "))
c=int(input("Enter the value :: "))
if (a<b and a<c):
  if(b<c):
    print(a,b,c);
  else:
    print(a,c,b);
elif(b<a and b<c):
  if(a<c):
    print(b,a,c);
  else:
    print(b,c,a);
elif(b<a):
  print(c,b,a); 
else:
  print(c,a,b);
