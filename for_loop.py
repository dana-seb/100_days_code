a = list(range(5))

# iterate through list
for i in range(len(a)):
    a[i] += 1
    print(i)

# iterate through list backwards
for i in range(len(a)-1, -1, -1):
   a[i] += 1
   print(i)