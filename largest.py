lst=[]
n=int(input())
for i in range(0,n):
  ele=int(input())
  lst.append(ele)
lt=[]
lst.sort(reverse=True)
lt.append(lst)
print(*lt)
