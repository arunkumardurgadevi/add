a,b = [int(x) for x in raw_input().split()]
a=int(a)
b=int(b)
for num in range(a+1,b):
  if(num%2==0):
    print(num),
