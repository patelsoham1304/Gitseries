re = [1,4]
count = 0
a = int(input("Enter the number you want:"))
l = []
for i in range(a):
    p = []
    for j in range(2):
        b = int(input("Enter the elements:"))
        p.append(b)
    l.append(p)
print(l)

for i in l:
    for j in i:
        for k in re:
            if j == k:
                count+=1
    print(count,"count")



    