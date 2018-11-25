for i in range(1,11):
  print(i*i)

for i in [1,3,5,7,9]:
    print(i, ":", i**3)

x = 2
y = 10
for j in range (0, y, x):
    print(j, end=" ")

ans = 0
for i in range(1, 11):
    ans = ans + i*i
    print(i)
print(ans)
