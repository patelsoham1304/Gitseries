n = int(input("Enter the number:"))
li=[]
#hello asad gadha hai
#jaapu gadha hai
for i in range(n):
    k = int(input("Enter the number:"))
    li.append(k)
print("The number you entered are:",li)

ch = int(input("Enter 1 to find the sum of the numbers or 2 to find the product of the numbers:"))
re = 0
match ch:
    case 1:
        for i in li:
            re+=i
        print(re)
    case 2:
        re=li.pop(0)
        for i in li:
            re-=i
        print(re)

    case 3:
        re=1
        for i in li:
            re*=i
        print(re)

    case 4:
        re=li.pop(0)
        for i in li:
            re/i
        print(re)
