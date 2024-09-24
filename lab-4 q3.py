x=int(input("enter the size of singer "))

l1= {(input()) for y in range(x)}
print(l1)

z=int(input("enter the size of dancers "))

l2={ input() for y in range(z)  }
print(l2)

#all artist of class
c=l1 |l2
print(c)

d=l1 & l2
print(d)

e=l1-l2
f=l2-l1
