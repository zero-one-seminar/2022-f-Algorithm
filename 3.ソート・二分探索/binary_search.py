a = [2, 4, 6, 8, 10, 12, 14, 16]
x = 8
l = 0
r = len(a)

while(r-l > 1):
  m = (l+r)//2
  if(a[m] == x):
    print(m)
    break
  elif a[m] < x:
    l = m
  else:
    r = m